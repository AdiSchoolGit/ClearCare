# 3/18/2026
Created front end dev log. 
    -   Deletion of old src folder and creation of new src folder with a template landing page. 
    -   Found issues in running this template with compatibility with with turbopack.
    -   Debugged issue by downgrading Next.js to 14.x 
    -   with downgrade needed to change the next.config.ts to .js and change syntax 
    -   landing page template worked as desired with "npm run dev" in src directory

# 3/19/2026
Customized the Landing page with our color scheme. Created a branch for frontEnd developing
    -   Deleted unnecesary images/text from template
    -   Centered everything and created a login button
    -   login button should link to the login page

# 3/20/2026
Linked the landing page, login page, and dashboard page. Basic customization for each page as well. Found issues with the linking pages but and tried installing react-rouetr-dom but is not needed 
    -   only needed import Link in order to link pages
    -   needed to create separate folders for each page so they can correctly route
    -   flow is now: landing page -> login -> dashboard
    -   Created the login page and added input fields (for future use)
    -   Created a dashboard page with a nav bar (for future use)