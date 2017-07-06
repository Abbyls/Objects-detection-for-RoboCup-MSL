# This Python file uses the following encoding: utf-8
"""autogenerated by genpy from nubot_common/WorldModelInfo.msg. Do not edit."""
import sys
python3 = True if sys.hexversion > 0x03000000 else False
import genpy
import struct

import nubot_common.msg
import std_msgs.msg

class WorldModelInfo(genpy.Message):
  _md5sum = "7d184d155b8f964299d2ae834875aebd"
  _type = "nubot_common/WorldModelInfo"
  _has_header = True #flag to mark the presence of a Header object
  _full_text = """Header header
ObstaclesInfo obstacleinfo
ObstaclesInfo oppinfo
RobotInfo[]   robotinfo
BallInfo[]    ballinfo
CoachInfo     coachinfo
PassCommands  pass_cmd


================================================================================
MSG: std_msgs/Header
# Standard metadata for higher-level stamped data types.
# This is generally used to communicate timestamped data 
# in a particular coordinate frame.
# 
# sequence ID: consecutively increasing ID 
uint32 seq
#Two-integer timestamp that is expressed as:
# * stamp.sec: seconds (stamp_secs) since epoch (in Python the variable is called 'secs')
# * stamp.nsec: nanoseconds since stamp_secs (in Python the variable is called 'nsecs')
# time-handling sugar is provided by the client library
time stamp
#Frame this data is associated with
# 0: no frame
# 1: global frame
string frame_id

================================================================================
MSG: nubot_common/ObstaclesInfo
Header header
Point2d[] pos
PPoint[] polar_pos


================================================================================
MSG: nubot_common/Point2d
float32 x
float32 y

================================================================================
MSG: nubot_common/PPoint
float32 angle
float32 radius

================================================================================
MSG: nubot_common/RobotInfo
Header header
int32    AgentID
int32    targetNum1
int32    targetNum2
int32    targetNum3
int32    targetNum4
int32    staticpassNum
int32    staticcatchNum
Point2d  pos
Angle    heading
float32  vrot
Point2d  vtrans
bool     iskick     
bool     isvalid 
bool     isstuck 
bool     isdribble
char     current_role
float32  role_time
Point2d  target
 

================================================================================
MSG: nubot_common/Angle
float32 theta

================================================================================
MSG: nubot_common/BallInfo
Header header
int32     ballinfostate
Point2d   pos
PPoint    real_pos
Point2d   velocity
bool      pos_known
bool      velocity_known


================================================================================
MSG: nubot_common/CoachInfo
Header header
char MatchMode
char MatchType
char TestMode           
Point2d pointA
Point2d pointB
int16 angleA
int16 angleB
char idA
char idB
char kickforce

================================================================================
MSG: nubot_common/PassCommands
uint32  pass_id
uint32  catch_id
Point2d pass_pt
Point2d catch_pt
bool    is_passout
bool    is_dynamic_pass
bool    is_static_pass
bool    is_valid
 
"""
  __slots__ = ['header','obstacleinfo','oppinfo','robotinfo','ballinfo','coachinfo','pass_cmd']
  _slot_types = ['std_msgs/Header','nubot_common/ObstaclesInfo','nubot_common/ObstaclesInfo','nubot_common/RobotInfo[]','nubot_common/BallInfo[]','nubot_common/CoachInfo','nubot_common/PassCommands']

  def __init__(self, *args, **kwds):
    """
    Constructor. Any message fields that are implicitly/explicitly
    set to None will be assigned a default value. The recommend
    use is keyword arguments as this is more robust to future message
    changes.  You cannot mix in-order arguments and keyword arguments.

    The available fields are:
       header,obstacleinfo,oppinfo,robotinfo,ballinfo,coachinfo,pass_cmd

    :param args: complete set of field values, in .msg order
    :param kwds: use keyword arguments corresponding to message field names
    to set specific fields.
    """
    if args or kwds:
      super(WorldModelInfo, self).__init__(*args, **kwds)
      #message fields cannot be None, assign default values for those that are
      if self.header is None:
        self.header = std_msgs.msg.Header()
      if self.obstacleinfo is None:
        self.obstacleinfo = nubot_common.msg.ObstaclesInfo()
      if self.oppinfo is None:
        self.oppinfo = nubot_common.msg.ObstaclesInfo()
      if self.robotinfo is None:
        self.robotinfo = []
      if self.ballinfo is None:
        self.ballinfo = []
      if self.coachinfo is None:
        self.coachinfo = nubot_common.msg.CoachInfo()
      if self.pass_cmd is None:
        self.pass_cmd = nubot_common.msg.PassCommands()
    else:
      self.header = std_msgs.msg.Header()
      self.obstacleinfo = nubot_common.msg.ObstaclesInfo()
      self.oppinfo = nubot_common.msg.ObstaclesInfo()
      self.robotinfo = []
      self.ballinfo = []
      self.coachinfo = nubot_common.msg.CoachInfo()
      self.pass_cmd = nubot_common.msg.PassCommands()

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
      buff.write(_struct_3I.pack(_x.header.seq, _x.header.stamp.secs, _x.header.stamp.nsecs))
      _x = self.header.frame_id
      length = len(_x)
      if python3 or type(_x) == unicode:
        _x = _x.encode('utf-8')
        length = len(_x)
      if python3:
        buff.write(struct.pack('<I%sB'%length, length, *_x))
      else:
        buff.write(struct.pack('<I%ss'%length, length, _x))
      _x = self
      buff.write(_struct_3I.pack(_x.obstacleinfo.header.seq, _x.obstacleinfo.header.stamp.secs, _x.obstacleinfo.header.stamp.nsecs))
      _x = self.obstacleinfo.header.frame_id
      length = len(_x)
      if python3 or type(_x) == unicode:
        _x = _x.encode('utf-8')
        length = len(_x)
      if python3:
        buff.write(struct.pack('<I%sB'%length, length, *_x))
      else:
        buff.write(struct.pack('<I%ss'%length, length, _x))
      length = len(self.obstacleinfo.pos)
      buff.write(_struct_I.pack(length))
      for val1 in self.obstacleinfo.pos:
        _x = val1
        buff.write(_struct_2f.pack(_x.x, _x.y))
      length = len(self.obstacleinfo.polar_pos)
      buff.write(_struct_I.pack(length))
      for val1 in self.obstacleinfo.polar_pos:
        _x = val1
        buff.write(_struct_2f.pack(_x.angle, _x.radius))
      _x = self
      buff.write(_struct_3I.pack(_x.oppinfo.header.seq, _x.oppinfo.header.stamp.secs, _x.oppinfo.header.stamp.nsecs))
      _x = self.oppinfo.header.frame_id
      length = len(_x)
      if python3 or type(_x) == unicode:
        _x = _x.encode('utf-8')
        length = len(_x)
      if python3:
        buff.write(struct.pack('<I%sB'%length, length, *_x))
      else:
        buff.write(struct.pack('<I%ss'%length, length, _x))
      length = len(self.oppinfo.pos)
      buff.write(_struct_I.pack(length))
      for val1 in self.oppinfo.pos:
        _x = val1
        buff.write(_struct_2f.pack(_x.x, _x.y))
      length = len(self.oppinfo.polar_pos)
      buff.write(_struct_I.pack(length))
      for val1 in self.oppinfo.polar_pos:
        _x = val1
        buff.write(_struct_2f.pack(_x.angle, _x.radius))
      length = len(self.robotinfo)
      buff.write(_struct_I.pack(length))
      for val1 in self.robotinfo:
        _v1 = val1.header
        buff.write(_struct_I.pack(_v1.seq))
        _v2 = _v1.stamp
        _x = _v2
        buff.write(_struct_2I.pack(_x.secs, _x.nsecs))
        _x = _v1.frame_id
        length = len(_x)
        if python3 or type(_x) == unicode:
          _x = _x.encode('utf-8')
          length = len(_x)
        if python3:
          buff.write(struct.pack('<I%sB'%length, length, *_x))
        else:
          buff.write(struct.pack('<I%ss'%length, length, _x))
        _x = val1
        buff.write(_struct_7i.pack(_x.AgentID, _x.targetNum1, _x.targetNum2, _x.targetNum3, _x.targetNum4, _x.staticpassNum, _x.staticcatchNum))
        _v3 = val1.pos
        _x = _v3
        buff.write(_struct_2f.pack(_x.x, _x.y))
        _v4 = val1.heading
        buff.write(_struct_f.pack(_v4.theta))
        buff.write(_struct_f.pack(val1.vrot))
        _v5 = val1.vtrans
        _x = _v5
        buff.write(_struct_2f.pack(_x.x, _x.y))
        _x = val1
        buff.write(_struct_5Bf.pack(_x.iskick, _x.isvalid, _x.isstuck, _x.isdribble, _x.current_role, _x.role_time))
        _v6 = val1.target
        _x = _v6
        buff.write(_struct_2f.pack(_x.x, _x.y))
      length = len(self.ballinfo)
      buff.write(_struct_I.pack(length))
      for val1 in self.ballinfo:
        _v7 = val1.header
        buff.write(_struct_I.pack(_v7.seq))
        _v8 = _v7.stamp
        _x = _v8
        buff.write(_struct_2I.pack(_x.secs, _x.nsecs))
        _x = _v7.frame_id
        length = len(_x)
        if python3 or type(_x) == unicode:
          _x = _x.encode('utf-8')
          length = len(_x)
        if python3:
          buff.write(struct.pack('<I%sB'%length, length, *_x))
        else:
          buff.write(struct.pack('<I%ss'%length, length, _x))
        buff.write(_struct_i.pack(val1.ballinfostate))
        _v9 = val1.pos
        _x = _v9
        buff.write(_struct_2f.pack(_x.x, _x.y))
        _v10 = val1.real_pos
        _x = _v10
        buff.write(_struct_2f.pack(_x.angle, _x.radius))
        _v11 = val1.velocity
        _x = _v11
        buff.write(_struct_2f.pack(_x.x, _x.y))
        _x = val1
        buff.write(_struct_2B.pack(_x.pos_known, _x.velocity_known))
      _x = self
      buff.write(_struct_3I.pack(_x.coachinfo.header.seq, _x.coachinfo.header.stamp.secs, _x.coachinfo.header.stamp.nsecs))
      _x = self.coachinfo.header.frame_id
      length = len(_x)
      if python3 or type(_x) == unicode:
        _x = _x.encode('utf-8')
        length = len(_x)
      if python3:
        buff.write(struct.pack('<I%sB'%length, length, *_x))
      else:
        buff.write(struct.pack('<I%ss'%length, length, _x))
      _x = self
      buff.write(_struct_3B4f2h3B2I4f4B.pack(_x.coachinfo.MatchMode, _x.coachinfo.MatchType, _x.coachinfo.TestMode, _x.coachinfo.pointA.x, _x.coachinfo.pointA.y, _x.coachinfo.pointB.x, _x.coachinfo.pointB.y, _x.coachinfo.angleA, _x.coachinfo.angleB, _x.coachinfo.idA, _x.coachinfo.idB, _x.coachinfo.kickforce, _x.pass_cmd.pass_id, _x.pass_cmd.catch_id, _x.pass_cmd.pass_pt.x, _x.pass_cmd.pass_pt.y, _x.pass_cmd.catch_pt.x, _x.pass_cmd.catch_pt.y, _x.pass_cmd.is_passout, _x.pass_cmd.is_dynamic_pass, _x.pass_cmd.is_static_pass, _x.pass_cmd.is_valid))
    except struct.error as se: self._check_types(struct.error("%s: '%s' when writing '%s'" % (type(se), str(se), str(locals().get('_x', self)))))
    except TypeError as te: self._check_types(ValueError("%s: '%s' when writing '%s'" % (type(te), str(te), str(locals().get('_x', self)))))

  def deserialize(self, str):
    """
    unpack serialized message in str into this message instance
    :param str: byte array of serialized message, ``str``
    """
    try:
      if self.header is None:
        self.header = std_msgs.msg.Header()
      if self.obstacleinfo is None:
        self.obstacleinfo = nubot_common.msg.ObstaclesInfo()
      if self.oppinfo is None:
        self.oppinfo = nubot_common.msg.ObstaclesInfo()
      if self.robotinfo is None:
        self.robotinfo = None
      if self.ballinfo is None:
        self.ballinfo = None
      if self.coachinfo is None:
        self.coachinfo = nubot_common.msg.CoachInfo()
      if self.pass_cmd is None:
        self.pass_cmd = nubot_common.msg.PassCommands()
      end = 0
      _x = self
      start = end
      end += 12
      (_x.header.seq, _x.header.stamp.secs, _x.header.stamp.nsecs,) = _struct_3I.unpack(str[start:end])
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      start = end
      end += length
      if python3:
        self.header.frame_id = str[start:end].decode('utf-8')
      else:
        self.header.frame_id = str[start:end]
      _x = self
      start = end
      end += 12
      (_x.obstacleinfo.header.seq, _x.obstacleinfo.header.stamp.secs, _x.obstacleinfo.header.stamp.nsecs,) = _struct_3I.unpack(str[start:end])
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      start = end
      end += length
      if python3:
        self.obstacleinfo.header.frame_id = str[start:end].decode('utf-8')
      else:
        self.obstacleinfo.header.frame_id = str[start:end]
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      self.obstacleinfo.pos = []
      for i in range(0, length):
        val1 = nubot_common.msg.Point2d()
        _x = val1
        start = end
        end += 8
        (_x.x, _x.y,) = _struct_2f.unpack(str[start:end])
        self.obstacleinfo.pos.append(val1)
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      self.obstacleinfo.polar_pos = []
      for i in range(0, length):
        val1 = nubot_common.msg.PPoint()
        _x = val1
        start = end
        end += 8
        (_x.angle, _x.radius,) = _struct_2f.unpack(str[start:end])
        self.obstacleinfo.polar_pos.append(val1)
      _x = self
      start = end
      end += 12
      (_x.oppinfo.header.seq, _x.oppinfo.header.stamp.secs, _x.oppinfo.header.stamp.nsecs,) = _struct_3I.unpack(str[start:end])
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      start = end
      end += length
      if python3:
        self.oppinfo.header.frame_id = str[start:end].decode('utf-8')
      else:
        self.oppinfo.header.frame_id = str[start:end]
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      self.oppinfo.pos = []
      for i in range(0, length):
        val1 = nubot_common.msg.Point2d()
        _x = val1
        start = end
        end += 8
        (_x.x, _x.y,) = _struct_2f.unpack(str[start:end])
        self.oppinfo.pos.append(val1)
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      self.oppinfo.polar_pos = []
      for i in range(0, length):
        val1 = nubot_common.msg.PPoint()
        _x = val1
        start = end
        end += 8
        (_x.angle, _x.radius,) = _struct_2f.unpack(str[start:end])
        self.oppinfo.polar_pos.append(val1)
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      self.robotinfo = []
      for i in range(0, length):
        val1 = nubot_common.msg.RobotInfo()
        _v12 = val1.header
        start = end
        end += 4
        (_v12.seq,) = _struct_I.unpack(str[start:end])
        _v13 = _v12.stamp
        _x = _v13
        start = end
        end += 8
        (_x.secs, _x.nsecs,) = _struct_2I.unpack(str[start:end])
        start = end
        end += 4
        (length,) = _struct_I.unpack(str[start:end])
        start = end
        end += length
        if python3:
          _v12.frame_id = str[start:end].decode('utf-8')
        else:
          _v12.frame_id = str[start:end]
        _x = val1
        start = end
        end += 28
        (_x.AgentID, _x.targetNum1, _x.targetNum2, _x.targetNum3, _x.targetNum4, _x.staticpassNum, _x.staticcatchNum,) = _struct_7i.unpack(str[start:end])
        _v14 = val1.pos
        _x = _v14
        start = end
        end += 8
        (_x.x, _x.y,) = _struct_2f.unpack(str[start:end])
        _v15 = val1.heading
        start = end
        end += 4
        (_v15.theta,) = _struct_f.unpack(str[start:end])
        start = end
        end += 4
        (val1.vrot,) = _struct_f.unpack(str[start:end])
        _v16 = val1.vtrans
        _x = _v16
        start = end
        end += 8
        (_x.x, _x.y,) = _struct_2f.unpack(str[start:end])
        _x = val1
        start = end
        end += 9
        (_x.iskick, _x.isvalid, _x.isstuck, _x.isdribble, _x.current_role, _x.role_time,) = _struct_5Bf.unpack(str[start:end])
        val1.iskick = bool(val1.iskick)
        val1.isvalid = bool(val1.isvalid)
        val1.isstuck = bool(val1.isstuck)
        val1.isdribble = bool(val1.isdribble)
        _v17 = val1.target
        _x = _v17
        start = end
        end += 8
        (_x.x, _x.y,) = _struct_2f.unpack(str[start:end])
        self.robotinfo.append(val1)
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      self.ballinfo = []
      for i in range(0, length):
        val1 = nubot_common.msg.BallInfo()
        _v18 = val1.header
        start = end
        end += 4
        (_v18.seq,) = _struct_I.unpack(str[start:end])
        _v19 = _v18.stamp
        _x = _v19
        start = end
        end += 8
        (_x.secs, _x.nsecs,) = _struct_2I.unpack(str[start:end])
        start = end
        end += 4
        (length,) = _struct_I.unpack(str[start:end])
        start = end
        end += length
        if python3:
          _v18.frame_id = str[start:end].decode('utf-8')
        else:
          _v18.frame_id = str[start:end]
        start = end
        end += 4
        (val1.ballinfostate,) = _struct_i.unpack(str[start:end])
        _v20 = val1.pos
        _x = _v20
        start = end
        end += 8
        (_x.x, _x.y,) = _struct_2f.unpack(str[start:end])
        _v21 = val1.real_pos
        _x = _v21
        start = end
        end += 8
        (_x.angle, _x.radius,) = _struct_2f.unpack(str[start:end])
        _v22 = val1.velocity
        _x = _v22
        start = end
        end += 8
        (_x.x, _x.y,) = _struct_2f.unpack(str[start:end])
        _x = val1
        start = end
        end += 2
        (_x.pos_known, _x.velocity_known,) = _struct_2B.unpack(str[start:end])
        val1.pos_known = bool(val1.pos_known)
        val1.velocity_known = bool(val1.velocity_known)
        self.ballinfo.append(val1)
      _x = self
      start = end
      end += 12
      (_x.coachinfo.header.seq, _x.coachinfo.header.stamp.secs, _x.coachinfo.header.stamp.nsecs,) = _struct_3I.unpack(str[start:end])
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      start = end
      end += length
      if python3:
        self.coachinfo.header.frame_id = str[start:end].decode('utf-8')
      else:
        self.coachinfo.header.frame_id = str[start:end]
      _x = self
      start = end
      end += 54
      (_x.coachinfo.MatchMode, _x.coachinfo.MatchType, _x.coachinfo.TestMode, _x.coachinfo.pointA.x, _x.coachinfo.pointA.y, _x.coachinfo.pointB.x, _x.coachinfo.pointB.y, _x.coachinfo.angleA, _x.coachinfo.angleB, _x.coachinfo.idA, _x.coachinfo.idB, _x.coachinfo.kickforce, _x.pass_cmd.pass_id, _x.pass_cmd.catch_id, _x.pass_cmd.pass_pt.x, _x.pass_cmd.pass_pt.y, _x.pass_cmd.catch_pt.x, _x.pass_cmd.catch_pt.y, _x.pass_cmd.is_passout, _x.pass_cmd.is_dynamic_pass, _x.pass_cmd.is_static_pass, _x.pass_cmd.is_valid,) = _struct_3B4f2h3B2I4f4B.unpack(str[start:end])
      self.pass_cmd.is_passout = bool(self.pass_cmd.is_passout)
      self.pass_cmd.is_dynamic_pass = bool(self.pass_cmd.is_dynamic_pass)
      self.pass_cmd.is_static_pass = bool(self.pass_cmd.is_static_pass)
      self.pass_cmd.is_valid = bool(self.pass_cmd.is_valid)
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
      buff.write(_struct_3I.pack(_x.header.seq, _x.header.stamp.secs, _x.header.stamp.nsecs))
      _x = self.header.frame_id
      length = len(_x)
      if python3 or type(_x) == unicode:
        _x = _x.encode('utf-8')
        length = len(_x)
      if python3:
        buff.write(struct.pack('<I%sB'%length, length, *_x))
      else:
        buff.write(struct.pack('<I%ss'%length, length, _x))
      _x = self
      buff.write(_struct_3I.pack(_x.obstacleinfo.header.seq, _x.obstacleinfo.header.stamp.secs, _x.obstacleinfo.header.stamp.nsecs))
      _x = self.obstacleinfo.header.frame_id
      length = len(_x)
      if python3 or type(_x) == unicode:
        _x = _x.encode('utf-8')
        length = len(_x)
      if python3:
        buff.write(struct.pack('<I%sB'%length, length, *_x))
      else:
        buff.write(struct.pack('<I%ss'%length, length, _x))
      length = len(self.obstacleinfo.pos)
      buff.write(_struct_I.pack(length))
      for val1 in self.obstacleinfo.pos:
        _x = val1
        buff.write(_struct_2f.pack(_x.x, _x.y))
      length = len(self.obstacleinfo.polar_pos)
      buff.write(_struct_I.pack(length))
      for val1 in self.obstacleinfo.polar_pos:
        _x = val1
        buff.write(_struct_2f.pack(_x.angle, _x.radius))
      _x = self
      buff.write(_struct_3I.pack(_x.oppinfo.header.seq, _x.oppinfo.header.stamp.secs, _x.oppinfo.header.stamp.nsecs))
      _x = self.oppinfo.header.frame_id
      length = len(_x)
      if python3 or type(_x) == unicode:
        _x = _x.encode('utf-8')
        length = len(_x)
      if python3:
        buff.write(struct.pack('<I%sB'%length, length, *_x))
      else:
        buff.write(struct.pack('<I%ss'%length, length, _x))
      length = len(self.oppinfo.pos)
      buff.write(_struct_I.pack(length))
      for val1 in self.oppinfo.pos:
        _x = val1
        buff.write(_struct_2f.pack(_x.x, _x.y))
      length = len(self.oppinfo.polar_pos)
      buff.write(_struct_I.pack(length))
      for val1 in self.oppinfo.polar_pos:
        _x = val1
        buff.write(_struct_2f.pack(_x.angle, _x.radius))
      length = len(self.robotinfo)
      buff.write(_struct_I.pack(length))
      for val1 in self.robotinfo:
        _v23 = val1.header
        buff.write(_struct_I.pack(_v23.seq))
        _v24 = _v23.stamp
        _x = _v24
        buff.write(_struct_2I.pack(_x.secs, _x.nsecs))
        _x = _v23.frame_id
        length = len(_x)
        if python3 or type(_x) == unicode:
          _x = _x.encode('utf-8')
          length = len(_x)
        if python3:
          buff.write(struct.pack('<I%sB'%length, length, *_x))
        else:
          buff.write(struct.pack('<I%ss'%length, length, _x))
        _x = val1
        buff.write(_struct_7i.pack(_x.AgentID, _x.targetNum1, _x.targetNum2, _x.targetNum3, _x.targetNum4, _x.staticpassNum, _x.staticcatchNum))
        _v25 = val1.pos
        _x = _v25
        buff.write(_struct_2f.pack(_x.x, _x.y))
        _v26 = val1.heading
        buff.write(_struct_f.pack(_v26.theta))
        buff.write(_struct_f.pack(val1.vrot))
        _v27 = val1.vtrans
        _x = _v27
        buff.write(_struct_2f.pack(_x.x, _x.y))
        _x = val1
        buff.write(_struct_5Bf.pack(_x.iskick, _x.isvalid, _x.isstuck, _x.isdribble, _x.current_role, _x.role_time))
        _v28 = val1.target
        _x = _v28
        buff.write(_struct_2f.pack(_x.x, _x.y))
      length = len(self.ballinfo)
      buff.write(_struct_I.pack(length))
      for val1 in self.ballinfo:
        _v29 = val1.header
        buff.write(_struct_I.pack(_v29.seq))
        _v30 = _v29.stamp
        _x = _v30
        buff.write(_struct_2I.pack(_x.secs, _x.nsecs))
        _x = _v29.frame_id
        length = len(_x)
        if python3 or type(_x) == unicode:
          _x = _x.encode('utf-8')
          length = len(_x)
        if python3:
          buff.write(struct.pack('<I%sB'%length, length, *_x))
        else:
          buff.write(struct.pack('<I%ss'%length, length, _x))
        buff.write(_struct_i.pack(val1.ballinfostate))
        _v31 = val1.pos
        _x = _v31
        buff.write(_struct_2f.pack(_x.x, _x.y))
        _v32 = val1.real_pos
        _x = _v32
        buff.write(_struct_2f.pack(_x.angle, _x.radius))
        _v33 = val1.velocity
        _x = _v33
        buff.write(_struct_2f.pack(_x.x, _x.y))
        _x = val1
        buff.write(_struct_2B.pack(_x.pos_known, _x.velocity_known))
      _x = self
      buff.write(_struct_3I.pack(_x.coachinfo.header.seq, _x.coachinfo.header.stamp.secs, _x.coachinfo.header.stamp.nsecs))
      _x = self.coachinfo.header.frame_id
      length = len(_x)
      if python3 or type(_x) == unicode:
        _x = _x.encode('utf-8')
        length = len(_x)
      if python3:
        buff.write(struct.pack('<I%sB'%length, length, *_x))
      else:
        buff.write(struct.pack('<I%ss'%length, length, _x))
      _x = self
      buff.write(_struct_3B4f2h3B2I4f4B.pack(_x.coachinfo.MatchMode, _x.coachinfo.MatchType, _x.coachinfo.TestMode, _x.coachinfo.pointA.x, _x.coachinfo.pointA.y, _x.coachinfo.pointB.x, _x.coachinfo.pointB.y, _x.coachinfo.angleA, _x.coachinfo.angleB, _x.coachinfo.idA, _x.coachinfo.idB, _x.coachinfo.kickforce, _x.pass_cmd.pass_id, _x.pass_cmd.catch_id, _x.pass_cmd.pass_pt.x, _x.pass_cmd.pass_pt.y, _x.pass_cmd.catch_pt.x, _x.pass_cmd.catch_pt.y, _x.pass_cmd.is_passout, _x.pass_cmd.is_dynamic_pass, _x.pass_cmd.is_static_pass, _x.pass_cmd.is_valid))
    except struct.error as se: self._check_types(struct.error("%s: '%s' when writing '%s'" % (type(se), str(se), str(locals().get('_x', self)))))
    except TypeError as te: self._check_types(ValueError("%s: '%s' when writing '%s'" % (type(te), str(te), str(locals().get('_x', self)))))

  def deserialize_numpy(self, str, numpy):
    """
    unpack serialized message in str into this message instance using numpy for array types
    :param str: byte array of serialized message, ``str``
    :param numpy: numpy python module
    """
    try:
      if self.header is None:
        self.header = std_msgs.msg.Header()
      if self.obstacleinfo is None:
        self.obstacleinfo = nubot_common.msg.ObstaclesInfo()
      if self.oppinfo is None:
        self.oppinfo = nubot_common.msg.ObstaclesInfo()
      if self.robotinfo is None:
        self.robotinfo = None
      if self.ballinfo is None:
        self.ballinfo = None
      if self.coachinfo is None:
        self.coachinfo = nubot_common.msg.CoachInfo()
      if self.pass_cmd is None:
        self.pass_cmd = nubot_common.msg.PassCommands()
      end = 0
      _x = self
      start = end
      end += 12
      (_x.header.seq, _x.header.stamp.secs, _x.header.stamp.nsecs,) = _struct_3I.unpack(str[start:end])
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      start = end
      end += length
      if python3:
        self.header.frame_id = str[start:end].decode('utf-8')
      else:
        self.header.frame_id = str[start:end]
      _x = self
      start = end
      end += 12
      (_x.obstacleinfo.header.seq, _x.obstacleinfo.header.stamp.secs, _x.obstacleinfo.header.stamp.nsecs,) = _struct_3I.unpack(str[start:end])
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      start = end
      end += length
      if python3:
        self.obstacleinfo.header.frame_id = str[start:end].decode('utf-8')
      else:
        self.obstacleinfo.header.frame_id = str[start:end]
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      self.obstacleinfo.pos = []
      for i in range(0, length):
        val1 = nubot_common.msg.Point2d()
        _x = val1
        start = end
        end += 8
        (_x.x, _x.y,) = _struct_2f.unpack(str[start:end])
        self.obstacleinfo.pos.append(val1)
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      self.obstacleinfo.polar_pos = []
      for i in range(0, length):
        val1 = nubot_common.msg.PPoint()
        _x = val1
        start = end
        end += 8
        (_x.angle, _x.radius,) = _struct_2f.unpack(str[start:end])
        self.obstacleinfo.polar_pos.append(val1)
      _x = self
      start = end
      end += 12
      (_x.oppinfo.header.seq, _x.oppinfo.header.stamp.secs, _x.oppinfo.header.stamp.nsecs,) = _struct_3I.unpack(str[start:end])
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      start = end
      end += length
      if python3:
        self.oppinfo.header.frame_id = str[start:end].decode('utf-8')
      else:
        self.oppinfo.header.frame_id = str[start:end]
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      self.oppinfo.pos = []
      for i in range(0, length):
        val1 = nubot_common.msg.Point2d()
        _x = val1
        start = end
        end += 8
        (_x.x, _x.y,) = _struct_2f.unpack(str[start:end])
        self.oppinfo.pos.append(val1)
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      self.oppinfo.polar_pos = []
      for i in range(0, length):
        val1 = nubot_common.msg.PPoint()
        _x = val1
        start = end
        end += 8
        (_x.angle, _x.radius,) = _struct_2f.unpack(str[start:end])
        self.oppinfo.polar_pos.append(val1)
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      self.robotinfo = []
      for i in range(0, length):
        val1 = nubot_common.msg.RobotInfo()
        _v34 = val1.header
        start = end
        end += 4
        (_v34.seq,) = _struct_I.unpack(str[start:end])
        _v35 = _v34.stamp
        _x = _v35
        start = end
        end += 8
        (_x.secs, _x.nsecs,) = _struct_2I.unpack(str[start:end])
        start = end
        end += 4
        (length,) = _struct_I.unpack(str[start:end])
        start = end
        end += length
        if python3:
          _v34.frame_id = str[start:end].decode('utf-8')
        else:
          _v34.frame_id = str[start:end]
        _x = val1
        start = end
        end += 28
        (_x.AgentID, _x.targetNum1, _x.targetNum2, _x.targetNum3, _x.targetNum4, _x.staticpassNum, _x.staticcatchNum,) = _struct_7i.unpack(str[start:end])
        _v36 = val1.pos
        _x = _v36
        start = end
        end += 8
        (_x.x, _x.y,) = _struct_2f.unpack(str[start:end])
        _v37 = val1.heading
        start = end
        end += 4
        (_v37.theta,) = _struct_f.unpack(str[start:end])
        start = end
        end += 4
        (val1.vrot,) = _struct_f.unpack(str[start:end])
        _v38 = val1.vtrans
        _x = _v38
        start = end
        end += 8
        (_x.x, _x.y,) = _struct_2f.unpack(str[start:end])
        _x = val1
        start = end
        end += 9
        (_x.iskick, _x.isvalid, _x.isstuck, _x.isdribble, _x.current_role, _x.role_time,) = _struct_5Bf.unpack(str[start:end])
        val1.iskick = bool(val1.iskick)
        val1.isvalid = bool(val1.isvalid)
        val1.isstuck = bool(val1.isstuck)
        val1.isdribble = bool(val1.isdribble)
        _v39 = val1.target
        _x = _v39
        start = end
        end += 8
        (_x.x, _x.y,) = _struct_2f.unpack(str[start:end])
        self.robotinfo.append(val1)
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      self.ballinfo = []
      for i in range(0, length):
        val1 = nubot_common.msg.BallInfo()
        _v40 = val1.header
        start = end
        end += 4
        (_v40.seq,) = _struct_I.unpack(str[start:end])
        _v41 = _v40.stamp
        _x = _v41
        start = end
        end += 8
        (_x.secs, _x.nsecs,) = _struct_2I.unpack(str[start:end])
        start = end
        end += 4
        (length,) = _struct_I.unpack(str[start:end])
        start = end
        end += length
        if python3:
          _v40.frame_id = str[start:end].decode('utf-8')
        else:
          _v40.frame_id = str[start:end]
        start = end
        end += 4
        (val1.ballinfostate,) = _struct_i.unpack(str[start:end])
        _v42 = val1.pos
        _x = _v42
        start = end
        end += 8
        (_x.x, _x.y,) = _struct_2f.unpack(str[start:end])
        _v43 = val1.real_pos
        _x = _v43
        start = end
        end += 8
        (_x.angle, _x.radius,) = _struct_2f.unpack(str[start:end])
        _v44 = val1.velocity
        _x = _v44
        start = end
        end += 8
        (_x.x, _x.y,) = _struct_2f.unpack(str[start:end])
        _x = val1
        start = end
        end += 2
        (_x.pos_known, _x.velocity_known,) = _struct_2B.unpack(str[start:end])
        val1.pos_known = bool(val1.pos_known)
        val1.velocity_known = bool(val1.velocity_known)
        self.ballinfo.append(val1)
      _x = self
      start = end
      end += 12
      (_x.coachinfo.header.seq, _x.coachinfo.header.stamp.secs, _x.coachinfo.header.stamp.nsecs,) = _struct_3I.unpack(str[start:end])
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      start = end
      end += length
      if python3:
        self.coachinfo.header.frame_id = str[start:end].decode('utf-8')
      else:
        self.coachinfo.header.frame_id = str[start:end]
      _x = self
      start = end
      end += 54
      (_x.coachinfo.MatchMode, _x.coachinfo.MatchType, _x.coachinfo.TestMode, _x.coachinfo.pointA.x, _x.coachinfo.pointA.y, _x.coachinfo.pointB.x, _x.coachinfo.pointB.y, _x.coachinfo.angleA, _x.coachinfo.angleB, _x.coachinfo.idA, _x.coachinfo.idB, _x.coachinfo.kickforce, _x.pass_cmd.pass_id, _x.pass_cmd.catch_id, _x.pass_cmd.pass_pt.x, _x.pass_cmd.pass_pt.y, _x.pass_cmd.catch_pt.x, _x.pass_cmd.catch_pt.y, _x.pass_cmd.is_passout, _x.pass_cmd.is_dynamic_pass, _x.pass_cmd.is_static_pass, _x.pass_cmd.is_valid,) = _struct_3B4f2h3B2I4f4B.unpack(str[start:end])
      self.pass_cmd.is_passout = bool(self.pass_cmd.is_passout)
      self.pass_cmd.is_dynamic_pass = bool(self.pass_cmd.is_dynamic_pass)
      self.pass_cmd.is_static_pass = bool(self.pass_cmd.is_static_pass)
      self.pass_cmd.is_valid = bool(self.pass_cmd.is_valid)
      return self
    except struct.error as e:
      raise genpy.DeserializationError(e) #most likely buffer underfill

_struct_I = genpy.struct_I
_struct_5Bf = struct.Struct("<5Bf")
_struct_f = struct.Struct("<f")
_struct_2f = struct.Struct("<2f")
_struct_7i = struct.Struct("<7i")
_struct_i = struct.Struct("<i")
_struct_3I = struct.Struct("<3I")
_struct_3B4f2h3B2I4f4B = struct.Struct("<3B4f2h3B2I4f4B")
_struct_2B = struct.Struct("<2B")
_struct_2I = struct.Struct("<2I")
