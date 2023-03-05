from odoo.tests.common import TransactionCase
from odoo.tests import tagged


@tagged('test_robot_sim')
class TestToyRobot(TransactionCase):
    def test_robot_simulator(self):
        robot_sims1 = self.env['toy.robot.sims'].create({
            'point_x': 0,
            'point_y': 0,
            'facing': 'n'
        }).set_move()
        self.assertTrue(robot_sims1)
        self.assertEqual(robot_sims1, 1)

