// Complete Instagram Follower Data Fetcher
// Run this in browser console while logged into Instagram

const username = "theumar_butt"; // Your Instagram username

(async () => {
  try {
    console.log(`Starting to fetch followers for ${username}...`);

    // Step 1: Get your user ID
    const userQueryRes = await fetch(
      `https://www.instagram.com/web/search/topsearch/?query=${username}`
    );
    const userQueryJson = await userQueryRes.json();
    
    const user = userQueryJson.users.map(u => u.user)
                                  .find(u => u.username === username);
    
    if (!user) {
      throw new Error(`User ${username} not found`);
    }

    const userId = user.pk;
    console.log(`Found user ID: ${userId}`);

    // Step 2: Fetch all followers
    const followers = [];
    let after = null;
    let hasNextPage = true;
    let pageCount = 0;

    const query_hash = 'c76146de99bb02f6415203be841dd25a';
    
    while (hasNextPage) {
      pageCount++;
      console.log(`Fetching page ${pageCount}...`);

      const variables = {
        id: userId,
        include_reel: true,
        fetch_mutual: false,
        first: 100, // You can increase this, but 100 is usually safe
        after: after
      };

      const url = `https://www.instagram.com/graphql/query/?query_hash=${query_hash}&variables=${encodeURIComponent(JSON.stringify(variables))}`;
      
      const response = await fetch(url);
      const data = await response.json();

      if (!data.data || !data.data.user) {
        console.error('Unexpected API response:', data);
        break;
      }

      const edges = data.data.user.edge_followed_by.edges;
      
      // Process each follower and store username + profile URL
      edges.forEach(edge => {
        const follower = edge.node;
        followers.push({
          username: follower.username,
          profile_url: `https://instagram.com/${follower.username}`,
          full_name: follower.full_name,
          id: follower.id,
          is_private: follower.is_private,
          is_verified: follower.is_verified
        });
      });

      // Check if there are more pages
      hasNextPage = data.data.user.edge_followed_by.page_info.has_next_page;
      after = data.data.user.edge_followed_by.page_info.end_cursor;

      // Add a small delay to avoid rate limiting
      await new Promise(resolve => setTimeout(resolve, 500));
    }

    console.log(`\n✅ Successfully fetched ${followers.length} followers!`);

    // Step 3: Display results in different formats
    console.log('\n=== ALL FOLLOWERS DATA (as objects) ===');
    console.log(followers);

    console.log('\n=== USERNAMES ONLY ===');
    const usernames = followers.map(f => f.username);
    console.log(usernames);

    console.log('\n=== USERNAME + PROFILE URL (requested format) ===');
    const usernameWithUrls = followers.map(f => `${f.username} - ${f.profile_url}`);
    console.log(usernameWithUrls.join('\n'));

    // Step 4: Create easy copy functions
    console.log('\n=== QUICK COPY COMMANDS ===');
    console.log('Copy usernames only: copy(followers.map(f => f.username))');
    console.log('Copy username + URLs: copy(followers.map(f => `${f.username} - ${f.profile_url}`))');
    console.log('Copy full data: copy(followers)');

    // Step 5: Make data available globally for copying
    window.followersData = followers;
    window.getUsernames = () => followers.map(f => f.username);
    window.getUsernamesWithUrls = () => followers.map(f => `${f.username} - ${f.profile_url}`);

    // Step 6: JSON Export Function
    window.exportFollowersJSON = () => {
      // Get current date for filename
      const now = new Date();
      const day = String(now.getDate()).padStart(2, '0');
      const month = String(now.getMonth() + 1).padStart(2, '0'); // Months are 0-based
      const year = now.getFullYear();
      
      // Create the data structure for JSON export
      const exportData = {
        metadata: {
          exported_at: now.toISOString(),
          export_timestamp: now.getTime(),
          target_username: username,
          total_followers: followers.length,
          source: "Instagram Follower Exporter"
        },
        followers: followers.map(follower => ({
          username: follower.username,
          profile_url: follower.profile_url,
          id: follower.id,
          full_name: follower.full_name,
          is_private: follower.is_private,
          is_verified: follower.is_verified
        }))
      };

      // Convert to JSON string with pretty formatting
      const jsonString = JSON.stringify(exportData, null, 2);
      
      // Create and download the file
      const blob = new Blob([jsonString], { type: 'application/json' });
      const url = window.URL.createObjectURL(blob);
      const a = document.createElement('a');
      a.href = url;
      a.download = `followers-${day}-${month}-${year}.json`;
      document.body.appendChild(a);
      a.click();
      document.body.removeChild(a);
      window.URL.revokeObjectURL(url);
      
      console.log(`✅ JSON file downloaded: followers-${day}-${month}-${year}.json`);
      console.log(`📊 Contains data for ${followers.length} followers`);
    };

    // Step 7: Summary
    console.log('\n=== SUMMARY ===');
    console.log(`Total followers: ${followers.length}`);
    console.log(`Private accounts: ${followers.filter(f => f.is_private).length}`);
    console.log(`Verified accounts: ${followers.filter(f => f.is_verified).length}`);
    
    // Keep the original CSV function for compatibility
    window.downloadCSV = () => {
      const headers = ['Username', 'Profile URL', 'Full Name', 'ID', 'Private', 'Verified'];
      const csvContent = [
        headers.join(','),
        ...followers.map(f => 
          `"${f.username}","${f.profile_url}","${f.full_name.replace(/"/g, '""')}","${f.id}","${f.is_private}","${f.is_verified}"`
        )
      ].join('\n');
      
      const blob = new Blob([csvContent], { type: 'text/csv' });
      const url = window.URL.createObjectURL(blob);
      const a = document.createElement('a');
      a.href = url;
      a.download = `instagram_followers_${username}.csv`;
      a.click();
      console.log('CSV download started!');
    };

    console.log('\n💡 Use exportFollowersJSON() to download as JSON file with date stamp');
    console.log('💡 Use downloadCSV() to download as CSV file (legacy function)');

  } catch (error) {
    console.error('Error fetching followers:', error);
    console.log('Make sure you are logged into Instagram and try again.');
  }
})();