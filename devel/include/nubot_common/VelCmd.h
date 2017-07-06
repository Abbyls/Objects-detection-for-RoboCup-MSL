// Generated by gencpp from file nubot_common/VelCmd.msg
// DO NOT EDIT!


#ifndef NUBOT_COMMON_MESSAGE_VELCMD_H
#define NUBOT_COMMON_MESSAGE_VELCMD_H


#include <string>
#include <vector>
#include <map>

#include <ros/types.h>
#include <ros/serialization.h>
#include <ros/builtin_message_traits.h>
#include <ros/message_operations.h>

#include <nubot_common/Point2d.h>
#include <nubot_common/Point2d.h>
#include <nubot_common/Point2d.h>

namespace nubot_common
{
template <class ContainerAllocator>
struct VelCmd_
{
  typedef VelCmd_<ContainerAllocator> Type;

  VelCmd_()
    : target()
    , target_ori(0.0)
    , target_vel()
    , maxvel(0.0)
    , maxw(0.0)
    , robot_pos()
    , robot_ori(0.0)
    , move_action(0)
    , rotate_acton(0)  {
    }
  VelCmd_(const ContainerAllocator& _alloc)
    : target(_alloc)
    , target_ori(0.0)
    , target_vel(_alloc)
    , maxvel(0.0)
    , maxw(0.0)
    , robot_pos(_alloc)
    , robot_ori(0.0)
    , move_action(0)
    , rotate_acton(0)  {
  (void)_alloc;
    }



   typedef  ::nubot_common::Point2d_<ContainerAllocator>  _target_type;
  _target_type target;

   typedef float _target_ori_type;
  _target_ori_type target_ori;

   typedef  ::nubot_common::Point2d_<ContainerAllocator>  _target_vel_type;
  _target_vel_type target_vel;

   typedef float _maxvel_type;
  _maxvel_type maxvel;

   typedef float _maxw_type;
  _maxw_type maxw;

   typedef  ::nubot_common::Point2d_<ContainerAllocator>  _robot_pos_type;
  _robot_pos_type robot_pos;

   typedef float _robot_ori_type;
  _robot_ori_type robot_ori;

   typedef uint8_t _move_action_type;
  _move_action_type move_action;

   typedef uint8_t _rotate_acton_type;
  _rotate_acton_type rotate_acton;




  typedef boost::shared_ptr< ::nubot_common::VelCmd_<ContainerAllocator> > Ptr;
  typedef boost::shared_ptr< ::nubot_common::VelCmd_<ContainerAllocator> const> ConstPtr;

}; // struct VelCmd_

typedef ::nubot_common::VelCmd_<std::allocator<void> > VelCmd;

typedef boost::shared_ptr< ::nubot_common::VelCmd > VelCmdPtr;
typedef boost::shared_ptr< ::nubot_common::VelCmd const> VelCmdConstPtr;

// constants requiring out of line definition



template<typename ContainerAllocator>
std::ostream& operator<<(std::ostream& s, const ::nubot_common::VelCmd_<ContainerAllocator> & v)
{
ros::message_operations::Printer< ::nubot_common::VelCmd_<ContainerAllocator> >::stream(s, "", v);
return s;
}

} // namespace nubot_common

namespace ros
{
namespace message_traits
{



// BOOLTRAITS {'IsFixedSize': True, 'IsMessage': True, 'HasHeader': False}
// {'geometry_msgs': ['/opt/ros/jade/share/geometry_msgs/cmake/../msg'], 'nubot_common': ['/home/ubuntu/libfreenect2-master/src/nubot_common/msgs'], 'std_msgs': ['/opt/ros/jade/share/std_msgs/cmake/../msg']}

// !!!!!!!!!!! ['__class__', '__delattr__', '__dict__', '__doc__', '__eq__', '__format__', '__getattribute__', '__hash__', '__init__', '__module__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', '__weakref__', '_parsed_fields', 'constants', 'fields', 'full_name', 'has_header', 'header_present', 'names', 'package', 'parsed_fields', 'short_name', 'text', 'types']




template <class ContainerAllocator>
struct IsFixedSize< ::nubot_common::VelCmd_<ContainerAllocator> >
  : TrueType
  { };

template <class ContainerAllocator>
struct IsFixedSize< ::nubot_common::VelCmd_<ContainerAllocator> const>
  : TrueType
  { };

template <class ContainerAllocator>
struct IsMessage< ::nubot_common::VelCmd_<ContainerAllocator> >
  : TrueType
  { };

template <class ContainerAllocator>
struct IsMessage< ::nubot_common::VelCmd_<ContainerAllocator> const>
  : TrueType
  { };

template <class ContainerAllocator>
struct HasHeader< ::nubot_common::VelCmd_<ContainerAllocator> >
  : FalseType
  { };

template <class ContainerAllocator>
struct HasHeader< ::nubot_common::VelCmd_<ContainerAllocator> const>
  : FalseType
  { };


template<class ContainerAllocator>
struct MD5Sum< ::nubot_common::VelCmd_<ContainerAllocator> >
{
  static const char* value()
  {
    return "24f8f6a4f2243802ffe8d3de8b91cf6b";
  }

  static const char* value(const ::nubot_common::VelCmd_<ContainerAllocator>&) { return value(); }
  static const uint64_t static_value1 = 0x24f8f6a4f2243802ULL;
  static const uint64_t static_value2 = 0xffe8d3de8b91cf6bULL;
};

template<class ContainerAllocator>
struct DataType< ::nubot_common::VelCmd_<ContainerAllocator> >
{
  static const char* value()
  {
    return "nubot_common/VelCmd";
  }

  static const char* value(const ::nubot_common::VelCmd_<ContainerAllocator>&) { return value(); }
};

template<class ContainerAllocator>
struct Definition< ::nubot_common::VelCmd_<ContainerAllocator> >
{
  static const char* value()
  {
    return "Point2d target\n\
float32 target_ori\n\
Point2d target_vel\n\
float32 maxvel\n\
float32 maxw\n\
Point2d robot_pos\n\
float32   robot_ori\n\
char    move_action\n\
char    rotate_acton\n\
\n\
================================================================================\n\
MSG: nubot_common/Point2d\n\
float32 x\n\
float32 y\n\
";
  }

  static const char* value(const ::nubot_common::VelCmd_<ContainerAllocator>&) { return value(); }
};

} // namespace message_traits
} // namespace ros

namespace ros
{
namespace serialization
{

  template<class ContainerAllocator> struct Serializer< ::nubot_common::VelCmd_<ContainerAllocator> >
  {
    template<typename Stream, typename T> inline static void allInOne(Stream& stream, T m)
    {
      stream.next(m.target);
      stream.next(m.target_ori);
      stream.next(m.target_vel);
      stream.next(m.maxvel);
      stream.next(m.maxw);
      stream.next(m.robot_pos);
      stream.next(m.robot_ori);
      stream.next(m.move_action);
      stream.next(m.rotate_acton);
    }

    ROS_DECLARE_ALLINONE_SERIALIZER
  }; // struct VelCmd_

} // namespace serialization
} // namespace ros

namespace ros
{
namespace message_operations
{

template<class ContainerAllocator>
struct Printer< ::nubot_common::VelCmd_<ContainerAllocator> >
{
  template<typename Stream> static void stream(Stream& s, const std::string& indent, const ::nubot_common::VelCmd_<ContainerAllocator>& v)
  {
    s << indent << "target: ";
    s << std::endl;
    Printer< ::nubot_common::Point2d_<ContainerAllocator> >::stream(s, indent + "  ", v.target);
    s << indent << "target_ori: ";
    Printer<float>::stream(s, indent + "  ", v.target_ori);
    s << indent << "target_vel: ";
    s << std::endl;
    Printer< ::nubot_common::Point2d_<ContainerAllocator> >::stream(s, indent + "  ", v.target_vel);
    s << indent << "maxvel: ";
    Printer<float>::stream(s, indent + "  ", v.maxvel);
    s << indent << "maxw: ";
    Printer<float>::stream(s, indent + "  ", v.maxw);
    s << indent << "robot_pos: ";
    s << std::endl;
    Printer< ::nubot_common::Point2d_<ContainerAllocator> >::stream(s, indent + "  ", v.robot_pos);
    s << indent << "robot_ori: ";
    Printer<float>::stream(s, indent + "  ", v.robot_ori);
    s << indent << "move_action: ";
    Printer<uint8_t>::stream(s, indent + "  ", v.move_action);
    s << indent << "rotate_acton: ";
    Printer<uint8_t>::stream(s, indent + "  ", v.rotate_acton);
  }
};

} // namespace message_operations
} // namespace ros

#endif // NUBOT_COMMON_MESSAGE_VELCMD_H
