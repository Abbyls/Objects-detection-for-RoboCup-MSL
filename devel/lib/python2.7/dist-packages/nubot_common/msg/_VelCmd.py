# This Python file uses the following encoding: utf-8
"""autogenerated by genpy from nubot_common/VelCmd.msg. Do not edit."""
import sys
python3 = True if sys.hexversion > 0x03000000 else False
import genpy
import struct

import nubot_common.msg

class VelCmd(genpy.Message):
  _md5sum = "24f8f6a4f2243802ffe8d3de8b91cf6b"
  _type = "nubot_common/VelCmd"
  _has_header = False #flag to mark the presence of a Header object
  _full_text = """Point2d target
float32 target_ori
Point2d target_vel
float32 maxvel
float32 maxw
Point2d robot_pos
float32   robot_ori
char    move_action
char    rotate_acton

================================================================================
MSG: nubot_common/Point2d
float32 x
float32 y
"""
  __slots__ = ['target','target_ori','target_vel','maxvel','maxw','robot_pos','robot_ori','move_action','rotate_acton']
  _slot_types = ['nubot_common/Point2d','float32','nubot_common/Point2d','float32','float32','nubot_common/Point2d','float32','char','char']

  def __init__(self, *args, **kwds):
    """
    Constructor. Any message fields that are implicitly/explicitly
    set to None will be assigned a default value. The recommend
    use is keyword arguments as this is more robust to future message
    changes.  You cannot mix in-order arguments and keyword arguments.

    The available fields are:
       target,target_ori,target_vel,maxvel,maxw,robot_pos,robot_ori,move_action,rotate_acton

    :param args: complete set of field values, in .msg order
    :param kwds: use keyword arguments corresponding to message field names
    to set specific fields.
    """
    if args or kwds:
      super(VelCmd, self).__init__(*args, **kwds)
      #message fields cannot be None, assign default values for those that are
      if self.target is None:
        self.target = nubot_common.msg.Point2d()
      if self.target_ori is None:
        self.target_ori = 0.
      if self.target_vel is None:
        self.target_vel = nubot_common.msg.Point2d()
      if self.maxvel is None:
        self.maxvel = 0.
      if self.maxw is None:
        self.maxw = 0.
      if self.robot_pos is None:
        self.robot_pos = nubot_common.msg.Point2d()
      if self.robot_ori is None:
        self.robot_ori = 0.
      if self.move_action is None:
        self.move_action = 0
      if self.rotate_acton is None:
        self.rotate_acton = 0
    else:
      self.target = nubot_common.msg.Point2d()
      self.target_ori = 0.
      self.target_vel = nubot_common.msg.Point2d()
      self.maxvel = 0.
      self.maxw = 0.
      self.robot_pos = nubot_common.msg.Point2d()
      self.robot_ori = 0.
      self.move_action = 0
      self.rotate_acton = 0

  def _get_types(self):
    """
    internal API method
    """
    return self._slot_types

  def serialize(self, buff):
    """
    serialize message into buffer
    :param buff: buffer, ``StringIO``
    """
    try:
      _x = self
      buff.write(_struct_10f2B.pack(_x.target.x, _x.target.y, _x.target_ori, _x.target_vel.x, _x.target_vel.y, _x.maxvel, _x.maxw, _x.robot_pos.x, _x.robot_pos.y, _x.robot_ori, _x.move_action, _x.rotate_acton))
    except struct.error as se: self._check_types(struct.error("%s: '%s' when writing '%s'" % (type(se), str(se), str(locals().get('_x', self)))))
    except TypeError as te: self._check_types(ValueError("%s: '%s' when writing '%s'" % (type(te), str(te), str(locals().get('_x', self)))))

  def deserialize(self, str):
    """
    unpack serialized message in str into this message instance
    :param str: byte array of serialized message, ``str``
    """
    try:
      if self.target is None:
        self.target = nubot_common.msg.Point2d()
      if self.target_vel is None:
        self.target_vel = nubot_common.msg.Point2d()
      if self.robot_pos is None:
        self.robot_pos = nubot_common.msg.Point2d()
      end = 0
      _x = self
      start = end
      end += 42
      (_x.target.x, _x.target.y, _x.target_ori, _x.target_vel.x, _x.target_vel.y, _x.maxvel, _x.maxw, _x.robot_pos.x, _x.robot_pos.y, _x.robot_ori, _x.move_action, _x.rotate_acton,) = _struct_10f2B.unpack(str[start:end])
      return self
    except struct.error as e:
      raise genpy.DeserializationError(e) #most likely buffer underfill


  def serialize_numpy(self, buff, numpy):
    """
    serialize message with numpy array types into buffer
    :param buff: buffer, ``StringIO``
    :param numpy: numpy python module
    """
    try:
      _x = self
      buff.write(_struct_10f2B.pack(_x.target.x, _x.target.y, _x.target_ori, _x.target_vel.x, _x.target_vel.y, _x.maxvel, _x.maxw, _x.robot_pos.x, _x.robot_pos.y, _x.robot_ori, _x.move_action, _x.rotate_acton))
    except struct.error as se: self._check_types(struct.error("%s: '%s' when writing '%s'" % (type(se), str(se), str(locals().get('_x', self)))))
    except TypeError as te: self._check_types(ValueError("%s: '%s' when writing '%s'" % (type(te), str(te), str(locals().get('_x', self)))))

  def deserialize_numpy(self, str, numpy):
    """
    unpack serialized message in str into this message instance using numpy for array types
    :param str: byte array of serialized message, ``str``
    :param numpy: numpy python module
    """
    try:
      if self.target is None:
        self.target = nubot_common.msg.Point2d()
      if self.target_vel is None:
        self.target_vel = nubot_common.msg.Point2d()
      if self.robot_pos is None:
        self.robot_pos = nubot_common.msg.Point2d()
      end = 0
      _x = self
      start = end
      end += 42
      (_x.target.x, _x.target.y, _x.target_ori, _x.target_vel.x, _x.target_vel.y, _x.maxvel, _x.maxw, _x.robot_pos.x, _x.robot_pos.y, _x.robot_ori, _x.move_action, _x.rotate_acton,) = _struct_10f2B.unpack(str[start:end])
      return self
    except struct.error as e:
      raise genpy.DeserializationError(e) #most likely buffer underfill

_struct_I = genpy.struct_I
_struct_10f2B = struct.Struct("<10f2B")