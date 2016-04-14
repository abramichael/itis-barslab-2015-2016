from behave import *
from player import Player

@given(u'a new player')
def step_impl(context):
    context.player = Player()

@then(u'it should have 100 HP')
def step_impl(context):
    assert context.player.hp == 100

@then(u'it should have an ability to kick')
def step_impl(context):
    assert context.player.kick is not None
