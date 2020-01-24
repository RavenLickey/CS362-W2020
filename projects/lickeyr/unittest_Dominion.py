from unittest import TestCase
import testUtility
import Dominion
class TestCard(TestCase):
    def setUp(self):
        #Data Setup
        self.player_names = ["Annie","*Ben","*Carla"]
        self.players = testUtility.getPlayers(self.player_names)
        self.nV = testUtility.numVic(self.players)
        self.nC = testUtility.getCurses(self.players)
        self.box = testUtility.getBoxes(self.nV)
        self.supply_order = testUtility.getSupplyOrder()

        self.supply = testUtility.getSupply(self.box)
        testUtility.setSupply(self.supply, self.players, self.nV, self.nC)
        self.trash = []
        self.player = Dominion.Player('Annie')

    def test_init(self):
        #initialize test data
        self.setUp()
        cost = 1
        buypower = 5

        #instantiate the card object
        card = Dominion.Coin_card(self.player.name, cost, buypower)

        # Verify that the class variables have the expected values
        self.assertEqual('Annie', card.name)
        self.assertEqual(buypower, card.buypower)
        self.assertEqual(cost, card.cost)
        self.assertEqual("coin", card.category)
        self.assertEqual(0, card.vpoints)

    def test_react(self):
        pass