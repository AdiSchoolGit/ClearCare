app 
  - Stores the webserver 
  Folders:
    - Repositories <-- DB queries
    - Services <-- Logic handling, where to send user input
    - Routes <-- Interactions between the frontend and the services

  
# 3/14/26
  
Creation of clients folder within webserver app directory
  - Start implementation of Google Places API client (geocoding, nearby search)
      - nearby search caps search radius
      - only accepts search radius in meters, so convert miles to meters before passing to API
  - Returns JSON <-- Probably requires extra configuration to work with BSON which is the format that MongoDB uses
  - Create new .env file for API keys within the clients folder
  - Creation of constants folder within app directory
      Store constants e.g. distance conversions for usage within API client files
  
Service created
  - hospitalSearch.py 
      2 arguments required zip & radius in miles from 5 to 25, increments of 5 only. Should be handled by frontend with a dropdown menu. There exists a check within the service to ensure the radius is within the valid range. However preventing invalid input at the source ensures that the service is not called with unexpected values.
  - create service folder within app directory

  # 3/15/26
  
  Creation of utils folder within app directory
   - Create bsonHandling.py file within utils folders
    Handles future DB retrievals by converting BSON only objects to JSON for use in the frontend
    Using BasedPyRight language servers have issues with modifying the default signature of DefaultJSONProvider
    Relating to language server issues BSON imports are seen as missing modules, despite packaged with pymongo
      Attempted uninstalling BSON, pymongo then reinstalling pymongo only. 
      Error still highlighted despite this file still working
   - Create repositories folder
    - Create example repo file which implements the READ logic which will be used in services under actual GET methods
    - Modify normalizationHandling within utils to normalize lists as well which just goes through documents within a collection

   Create test folder
    - Configure PyTest within backend/pytext.ini
    - Creation of test files
      Must start or end with test_* or *_test to be valid
      @patch will include the functions being tested without importing them
    - Special case:
      To test actual API calls, use `pytest.mark.*` with `*` serving as a placeholder for the actual test function
      Which does require adding the marker to the `pytest.ini`
      USES ACTUAL API TOKENS from API key so use at own risk
      Currently max number of concurrent API calls is 20 from the geocoding API
