# -*- coding: utf-8 -*-

from unittest import TestCase
from datetime import datetime, date

from gitstats import get_contributions_for_user_for_dates

class GithubTests(TestCase):

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_contributions_five_days(self):
        """Test the contributions of the account Dogild for 5 days"""
        contributions = get_contributions_for_user_for_dates("Dogild", date(2014, 5, 4), date(2014, 5, 10), 32400)

        self.assertEqual(len(contributions), 7)

        contributions_04_05 = contributions[0]
        self.assertEqual(len(contributions_04_05), 0)

        contributions_05_05 = contributions[1]
        self.assertEqual(len(contributions_05_05), 4)
        self.assertEqual(str(contributions_05_05[0]).replace('\n', ''), "Commit : 2014-05-05 11:40:17 Alexandre Wilhelm Added option MODE=debug to launch cucumber without compiling the project".replace('\n', ''))
        self.assertEqual(str(contributions_05_05[1]).replace('\n', ''), "Commit : 2014-05-05 15:30:39 Alexandre Wilhelm Added logged for thin server".replace('\n', ''))
        self.assertEqual(str(contributions_05_05[2]).replace('\n', ''), "Commit : 2014-05-05 17:14:40 Alexandre Wilhelm Fixed bug with categories".replace('\n', ''))
        self.assertEqual(str(contributions_05_05[3]).replace('\n', ''), "Commit : 2014-05-05 07:50:16 Alexandre Wilhelm Fixed: fixed type in XcodeCapp".replace('\n', ''))

        contributions_06_05 = contributions[2]
        self.assertEqual(len(contributions_06_05), 9)
        self.assertEqual(str(contributions_06_05[0]).replace('\n', ''), "Commit : 2014-05-06 14:52:10 Alexandre Wilhelm Removed code who are not supposed to be in Cucapp".replace('\n', ''))
        self.assertEqual(str(contributions_06_05[1]).replace('\n', ''), "Commit : 2014-05-06 15:46:41 Alexandre Wilhelm Load dinamicly CucumberCategories in features".replace('\n', ''))
        self.assertEqual(str(contributions_06_05[2]).replace('\n', ''), "Commit : 2014-05-06 16:03:40 Alexandre Wilhelm Clean Cucapp".replace('\n', ''))
        self.assertEqual(str(contributions_06_05[3]).replace('\n', ''), "Commit : 2014-05-06 16:04:19 Alexandre Wilhelm Clean Cucapp".replace('\n', ''))
        self.assertEqual(str(contributions_06_05[4]).replace('\n', ''), "Commit : 2014-05-06 16:19:42 Alexandre Wilhelm Cleaned Cucapp".replace('\n', ''))
        self.assertEqual(str(contributions_06_05[5]).replace('\n', ''), "Commit : 2014-05-06 17:04:21 Alexandre Wilhelm Added var env to change the port of the server".replace('\n', ''))
        self.assertEqual(str(contributions_06_05[6]).replace('\n', ''), "Commit : 2014-05-06 17:24:54 Alexandre Wilhelm Changed debug to source".replace('\n', ''))
        self.assertEqual(str(contributions_06_05[7]).replace('\n', ''), "Commit : 2014-05-06 21:48:23 Alexandre Wilhelm Fixed: Jake clean in xCodeCappPreviously we used jake clean instead of jake clobber".replace('\n', ''))
        self.assertEqual(str(contributions_06_05[8]).replace('\n', ''), "Commit : 2014-05-06 21:49:49 Alexandre Wilhelm Merge remote-tracking branch 'origin' into xCodeCappUpdatingCapp".replace('\n', ''))

        contributions_07_05 = contributions[3]
        self.assertEqual(len(contributions_07_05), 3)
        self.assertEqual(str(contributions_07_05[0]).replace('\n', ''), "Commit : 2014-05-07 09:25:53 Alexandre Wilhelm Fixed bug about non source test".replace('\n', ''))
        self.assertEqual(str(contributions_07_05[1]).replace('\n', ''), "Commit : 2014-05-07 14:03:46 Alexandre Wilhelm Fixed bug".replace('\n', ''))
        self.assertEqual(str(contributions_07_05[2]).replace('\n', ''), "Commit : 2014-05-07 14:19:38 Alexandre Wilhelm Added possibility to have a app_directory var env".replace('\n', ''))

        contributions_08_05 = contributions[4]
        self.assertEqual(len(contributions_08_05), 5)
        self.assertEqual(str(contributions_08_05[0]).replace('\n', ''), "Commit : 2014-05-08 12:18:00 Alexandre Wilhelm Fixed typo".replace('\n', ''))
        self.assertEqual(str(contributions_08_05[1]).replace('\n', ''), "Commit : 2014-05-08 12:30:52 Alexandre Wilhelm New: add env var to launch the source or the compiled cucapp".replace('\n', ''))
        self.assertEqual(str(contributions_08_05[2]).replace('\n', ''), "Commit : 2014-05-08 07:56:06 Alexandre Wilhelm Fixed: type in preferences for the update of cappuccino".replace('\n', ''))
        self.assertEqual(str(contributions_08_05[3]).replace('\n', ''), "Commit : 2014-05-08 08:04:51 Alexandre Wilhelm Fixed: xCodeCapp documentation is outdatedFixes #2114".replace('\n', ''))
        self.assertEqual(str(contributions_08_05[4]).replace('\n', ''), "Commit : 2014-05-08 08:26:22 Alexandre Wilhelm Fixed: udpate file help.pages".replace('\n', ''))

        contributions_09_05 = contributions[5]
        self.assertEqual(len(contributions_09_05), 1)
        self.assertEqual(str(contributions_09_05[0]).replace('\n', ''), "Commit : 2014-05-09 12:50:58 Alexandre Wilhelm New: Added gem. You just need to do gem install cucapp to get everything you need for cucapp".replace('\n', ''))

        contributions_10_05 = contributions[6]
        self.assertEqual(len(contributions_10_05), 0)




