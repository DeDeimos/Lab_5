from behave import given, when, then, step
import last_lab.unique as unique

@given('a list of numbers')
def step_impl(context):
    context.list_of_numbers = [1, 2, 1, 3, 3, 2]

@when('we call Unique')
def step_impl(context):
    context.unique = unique.Unique(context.list_of_numbers)

@then('we get a list of unique numbers')
def step_iml(context):
    assert context.unique.items == [1, 2, 3]

@given('a list of strings')
def step_impl(context):
    context.list_of_strings = ["a", "A", "B", "b"]

@when('we call Unique with ignore_case=True')
def step_impl(context):
    context.unique2 = unique.Unique(context.list_of_strings, ignore_case=True)

@then('we get a list of unique strings')
def step_iml(context):
    print(context.unique2.items)
    assert context.unique2.items == ["a", "B"]