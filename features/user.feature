Feature: showing off behave

    Scenario: Run a simple test
        Given a list of numbers
        When we call Unique
        Then we get a list of unique numbers

        Given a list of strings
        When we call Unique with ignore_case=True
        Then we get a list of unique strings