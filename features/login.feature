Feature: Login Functionality

    As a user
    I want to login to Swag Labs
    So that I can access the inventory page


    Scenario: Successful Login With Valid Credentials

        Given The User Opens The Swag Labs Application
        When The User Enters Valid Login Credentials
        And The User Clicks The Login Button
        Then The User Should See The Inventory Page