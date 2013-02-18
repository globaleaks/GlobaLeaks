from twisted.internet.defer import inlineCallbacks
from twisted.trial import unittest

from globaleaks.settings import transact
from globaleaks.jobs import delivery_sched
from globaleaks.tests import helpers

from globaleaks.handlers.receiver import get_receiver_tip_list
from globaleaks.handlers.submission import finalize_submission

class TestJobs(helpers.TestGL):

    @inlineCallbacks
    def setUp(self):
        self.setUp_dummy()
        yield self.initalize_db()
    
    @inlineCallbacks
    def test_tip_creation(self):
        yield finalize_submission(self.dummySubmission['submission_gus'])
        yield delivery_sched.tip_creation()
        receiver_tips = yield get_receiver_tip_list(self.dummyReceiver['username'])

        expected_keys = ['access_counter', 'creation_date', 'expressed_pertinence', 'id', 'last_acesss']
        self.assertEqual(set(receiver_tips[0].keys()), set(expected_keys))
        
        
