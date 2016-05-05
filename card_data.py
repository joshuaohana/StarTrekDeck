
import CardTypes
print(CardTypes)
from CardTypes import Card
print(Card)
from CardTypes.Card import Card
#Is there an easier way to import from folders?^^^
cards = {'Duras': Card('Duras',0, 3, 1, 0, 7, 0, 0, 'You may trash 1 card in your hand or move 1 card from your hand to the top of another player\'s deck.', '"You would dare to insult my father\'s name?"')
    ,'Jean Luc Picard': Card('Jean Luc The Pussy Slayer',2,2,3,0,9,0,0, 'When you complete a Mission or diplomacy\na Starship, you may gain 1 card from starbase.', '"I think you\'ve got a great deal\nto learn from Starfleet...\nand my dick."'),
     'Wesley Crusher': Card('Wesley Crusher',1, 0, 1, 0, 4, 0, 0, 'You get +1 search.\nDuring your turn, you may upgrade this card to a\nFederation Character from starbase with a cost 8 or less.','"I\'m with Starfleet. We don\'t lie."'),
    'Geordi La Forge':Card('Geordi La Forge', 2,2,0,'Amount of damage that was removed\nfrom your flagship this turn +2.', 7,0, 0,'Remove up to 2 damage from your flagship.','"I need to get down to engineering and begin that analysis."'),
    'Data':Card('Data',2,2,0,0,7,0,0,'Draw 2 cards. Move 2 cards from your hand to the\ntop of your deck in any order.', '"My programming may be inadequate to the task."'),
    'Natasha Yar': Card('Natasha Yar',0, 2, 0, 0, 5, 0, 0, 'You may upgrade 1 Maneuver in your hand or bridgeto a Maneuver from starbase costing up to 2 more.', '"As Security Chief, I can\'t just stand here..."'),
    'William Riker': Card('William Riker',2,2,2,0,8,0,0,'Select 1 opponent. If you do, name a card.\nThat opponent must guess if you have that card in your hand.\nIf they guess wrong, you may have them peek at your hand,\nand you draw 2 cards.','"Poker...is that a game of some sort?"'),
    'Sela': Card('Sela',2,2,2,0,9,0,0, 'Name 1 card. Peek at each opponent\'s hand. If they have that card in their hand,\nthey must discard 1 copy of it.',
                 '"Humans have a way of showing up\nwhen you least expect them."'),
    'Beverly Crusher': Card('Beverly Crusher',1,0,2,0,5,0,0,'Move up to 2 Characters from your discard area\nto the top of your deck in any order.', '"I\'d like you to come to Sick Bay for some examinations."'),
    'Worf': Card('Worf',0,2,0,0,6,0,0,'You may upgrade 1 Maneuver or Setup in your hand or bridge\nto a Maneuver or Setup from starbase costing up to 2 more and move it to your hand.',
                 '"Klingons don\'t laugh."'),
    'Fire All Weapons': Card('Fire All Weapons', 0,7,0,0,7,0,0, None, 'FIRE ZE MISSILES'),
    'Warp Speed': Card('Warp Speed',5,0,0,0,6,0,0, 'You may discard 1 card from your hand.\nIf you do, draw 1 card.', '"I wanna go fast" -Ricky Bobby'),
    'Deanna Troi': Card('Deanna Troi',1,0,2,0,6,0,0,'Peek at 1 opponent\'s hand. Select 1 Character\n in their hand with a cost of 7 or less\nand they discard it.', '"You must have know I couldn\'t allow you to do that."'),
    'Ensign': Card('Ensign',0,1,0,0,1,1,0,'+1 XP', 'The bottom of the foodchain.'),
    'Lieutenant':Card('Commander',1,1,0,0,5,3,0,'+3 XP', 'Now we\'re talkin'),
    'Commander':Card('Commander',1,1,0,0,5,3,0,'+3 XP', 'Now we\'re talkin') }


# GeordiLaForge = Card('Geordi La Forge', 2,2,0,'Amount of damage that was removed\nfrom your flagship this turn +2.', 7,0, 0,
#                      'Remove up to 2 damage from your flagship.','"I need to get down to engineering and begin that analysis."')
#
# Data = Card('Data',2,2,0,0,7,0,0,'Draw 2 cards. Move 2 cards from your hand to the\ntop of your deck in any order.', '"My programming may be inadequate to the task."')
#
# NatashaYar = Card('Natasha Yar',0, 2, 0, 0, 5, 0, 0, 'You may upgrade 1 Maneuver in your hand or bridgeto a Maneuver from starbase costing up to 2 more.', '"As Security Chief, I can\'t just stand here..."')
#
# WilliamRiker = Card('William Riker',2,2,2,0,8,0,0,'Select 1 opponent. If you do, name a card.\nThat opponent must guess if you have that card in your hand.\nIf they guess wrong, you may have them peek at your hand,\nand you draw 2 cards.',
#                     '"Poker...is that a game of some sort?"')
#
# Sela = Card('Sela',2,2,2,0,9,0,0, 'Name 1 card. Peek at each opponent\'s hand. If they have that card in their hand,\nthey must discard 1 copy of it.',
#             '"Humans have a way of showing up\nwhen you least expect them."')
#
# BeverlyCrusher = Card('Beverly Crusher',1,0,2,0,5,0,0,'Move up to 2 Characters from your discard area\nto the top of your deck in any order.', '"I\'d like you to come to Sick Bay for some examinations."')
#
# Worf = Card('Worf',0,2,0,0,6,0,0,'You may upgrade 1 Maneuver or Setup in your hand or bridge\nto a Maneuver or Setup from starbase costing up to 2 more and move it to your hand.',
#             '"Klingons don\'t laugh."')
#
# JeanLucPicard = Card('Jean Luc The Pussy Slayer',2,2,3,0,9,0,0, 'When you complete a Mission or diplomacy\na Starship, you may gain 1 card from starbase.', '"I think you\'ve got a great deal\nto learn from Starfleet...\nand my dick."')
#
# FireAllWeapons = Card('Fire All Weapons', 0,7,0,0,7,0,0, None, 'FIRE ZE MISSILES')
#
# WarpSpeed = Card('Warp Speed',5,0,0,0,6,0,0, 'You may discard 1 card from your hand.\nIf you do, draw 1 card.', '"I wanna go fast" -Ricky Bobby')
#
# DeannaTroi = Card('Deanna Troi',1,0,2,0,6,0,0,'Peek at 1 opponent\'s hand. Select 1 Character\n in their hand with a cost of 7 or less\nand they discard it.', '"You must have know I couldn\'t allow you to do that."')
#
# Ensign = Card('Ensign',0,1,0,0,1,1,0,'+1 XP', 'The bottom of the foodchain.')
#
# Lieutenant = Card('Lieutenant',1,0,0,0,3,2,0,'+2 XP', 'Better than an Ensign.')
#
# Commander = Card('Commander',1,1,0,0,5,3,0,'+3 XP', 'Now we\'re talkin')
#
