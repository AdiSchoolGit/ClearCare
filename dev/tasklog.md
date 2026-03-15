1. Serve flask as `/api` instead of `/` when users enter url
  - Host a front end at port 3000
  - Create a dockerfile for a containerized react app
2. Create a folder within backend/app which acts as a wrapper for external API's
  - Google maps places API <-- requires extra security measures to prevent api call abuse
      Current development:
        - Integrate geocoding to take user defined Zip Code and turn it into coordinates
        - Integrate nearbysearch to find hospitals near the user's location
            Will possibly require additional fields to include such as "urgent care" or smaller clinics
        - API key requires 10$ min payment for the "pay as you go" payment model. If it is a subscription model then its a larger cost
  - Insurance verification API 
  - Hospital pricing API + CMS data
3. Configure database
  - Creating clusters and collections
  - CRUD + RESTful API based development within FLASK
