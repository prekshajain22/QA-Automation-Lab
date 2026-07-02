Feature: Login

    Scenario: Login with standard user
        Given I Open The Application
        When I Login Using User "standard_user"
        Then I Should See The Inventory Page