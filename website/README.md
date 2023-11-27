The full service will have three layers, as I’ve discussed earlier:
Web
    The web interface
Service
    The business logic
Data
    The precious DNA of the whole thing
Plus the web service will have these cross-layer components:

Model
    Pydantic data definitions
Tests
    Unit, integration, and end-to-end tests


Web Client <--->   Web
                    |---------  Model
                  Service
                    |    
                   Data  <---> Database