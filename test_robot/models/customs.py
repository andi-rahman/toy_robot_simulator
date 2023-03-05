from odoo import api, models, fields, _
from odoo.exceptions import ValidationError


class ToyRobotSims(models.Model):
    _name = 'toy.robot.sims'
    _description = "Toy Robot Simulator"

    point_x = fields.Integer(string="Point X", store=True)
    point_y = fields.Integer(string="Point Y", store=True)
    facing = fields.Selection([
    	('n', 'North'),
    	('s', 'South'),
    	('e', 'East'),
    	('w', 'West'),
    	], string='Facing', default='n', store=True)
    report = fields.Char(readonly=True, store=True)
    is_place = fields.Boolean(store=True, string="Is Place")

    def name_get(self):
        res = []
        for toy in self:
            name = _("%s,%s, %s") % (toy.point_x, toy.point_y, toy._get_facing(toy.facing))
            res.append((toy.id, name))
        return res

    def set_place(self):
        point_x = self.point_x or str(0)
        point_y = self.point_y or str(0)
        facing = dict(self._fields['facing']._description_selection(self.env))[self.facing]
        self.update({'report': _("%s,%s,%s") % (point_x, point_y, facing), 'is_place': True})
        return True

    def check_position(self, point_x, point_y, facing=False):
        if point_y < 0 or point_x < 0 or point_y > 5 or point_x > 5:
            raise ValidationError(_("You toy will fallen"))
        else:
            return True

    def _get_facing(self, facing):
        return dict(self._fields['facing']._description_selection(self.env))[facing]

    def set_move(self):
        point_x = self.point_x
        point_y = self.point_y
        facing = self._get_facing(self.facing)
        if self.facing:
            if self.facing == 'n':
                point_y += 1
                check_position = self.check_position(point_x, point_y)
                if check_position:
                    self.update({'report': _("%s,%s,%s") % (point_x, point_y, facing), 'point_y': point_y})
                    return point_y
            if self.facing == 'w':
                point_x -= 1
                check_position = self.check_position(point_x, point_y)
                if check_position:
                    self.update({'report': _("%s,%s,%s") % (point_x, point_y, facing), 'point_x': point_x})
                    return point_x
            if self.facing == 's':
                point_y -= 1
                check_position = self.check_position(point_x, point_y)
                if check_position:
                    self.update({'report': _("%s,%s,%s") % (point_x, point_y, facing), 'point_y': point_y})
                    return point_y
            if self.facing == 'e':
                point_x += 1
                check_position = self.check_position(point_x, point_y)
                if check_position:
                    self.update({'report': _("%s,%s,%s") % (point_x, point_y, facing), 'point_x': point_x})
                    return point_x

    def set_right_left(self):
        point_x = self.point_x
        point_y = self.point_y
        if self.facing == 'n':
            facing = self._get_facing('s')
            self.update({'report': _("%s,%s,%s") % (point_x, point_y, facing), 'facing': 's'})
            return True
        if self.facing == 's':
            facing = self._get_facing('n')
            self.update({'report': _("%s,%s,%s") % (point_x, point_y, facing), 'facing': 'n'})
            return True
        if self.facing == 'e':
            facing = self._get_facing('w')
            self.update({'report': _("%s,%s,%s") % (point_x, point_y, facing), 'facing': 'w'})
            return True
        if self.facing == 'w':
            facing = self._get_facing('e')
            self.update({'report': _("%s,%s,%s") % (point_x, point_y, facing), 'facing': 'e'})
            return True
