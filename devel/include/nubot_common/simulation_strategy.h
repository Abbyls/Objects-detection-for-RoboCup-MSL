// Generated by gencpp from file nubot_common/simulation_strategy.msg
// DO NOT EDIT!


#ifndef NUBOT_COMMON_MESSAGE_SIMULATION_STRATEGY_H
#define NUBOT_COMMON_MESSAGE_SIMULATION_STRATEGY_H


#include <string>
#include <vector>
#include <map>

#include <ros/types.h>
#include <ros/serialization.h>
#include <ros/builtin_message_traits.h>
#include <ros/message_operations.h>

#include <nubot_common/StrategyInfo.h>

namespace nubot_common
{
template <class ContainerAllocator>
struct simulation_strategy_
{
  typedef simulation_strategy_<ContainerAllocator> Type;

  simulation_strategy_()
    : strategy_msgs()  {
    }
  simulation_strategy_(const ContainerAllocator& _alloc)
    : strategy_msgs(_alloc)  {
  (void)_alloc;
    }



   typedef std::vector< ::nubot_common::StrategyInfo_<ContainerAllocator> , typename ContainerAllocator::template rebind< ::nubot_common::StrategyInfo_<ContainerAllocator> >::other >  _strategy_msgs_type;
  _strategy_msgs_type strategy_msgs;




  typedef boost::shared_ptr< ::nubot_common::simulation_strategy_<ContainerAllocator> > Ptr;
  typedef boost::shared_ptr< ::nubot_common::simulation_strategy_<ContainerAllocator> const> ConstPtr;

}; // struct simulation_strategy_

typedef ::nubot_common::simulation_strategy_<std::allocator<void> > simulation_strategy;

typedef boost::shared_ptr< ::nubot_common::simulation_strategy > simulation_strategyPtr;
typedef boost::shared_ptr< ::nubot_common::simulation_strategy const> simulation_strategyConstPtr;

// constants requiring out of line definition



template<typename ContainerAllocator>
std::ostream& operator<<(std::ostream& s, const ::nubot_common::simulation_strategy_<ContainerAllocator> & v)
{
ros::message_operations::Printer< ::nubot_common::simulation_strategy_<ContainerAllocator> >::stream(s, "", v);
return s;
}

} // namespace nubot_common

namespace ros
{
namespace message_traits
{



// BOOLTRAITS {'IsFixedSize': False, 'IsMessage': True, 'HasHeader': False}
// {'geometry_msgs': ['/opt/ros/jade/share/geometry_msgs/cmake/../msg'], 'nubot_common': ['/home/ubuntu/libfreenect2-master/src/nubot_common/msgs'], 'std_msgs': ['/opt/ros/jade/share/std_msgs/cmake/../msg']}

// !!!!!!!!!!! ['__class__', '__delattr__', '__dict__', '__doc__', '__eq__', '__format__', '__getattribute__', '__hash__', '__init__', '__module__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', '__weakref__', '_parsed_fields', 'constants', 'fields', 'full_name', 'has_header', 'header_present', 'names', 'package', 'parsed_fields', 'short_name', 'text', 'types']




template <class ContainerAllocator>
struct IsFixedSize< ::nubot_common::simulation_strategy_<ContainerAllocator> >
  : FalseType
  { };

template <class ContainerAllocator>
struct IsFixedSize< ::nubot_common::simulation_strategy_<ContainerAllocator> const>
  : FalseType
  { };

template <class ContainerAllocator>
struct IsMessage< ::nubot_common::simulation_strategy_<ContainerAllocator> >
  : TrueType
  { };

template <class ContainerAllocator>
struct IsMessage< ::nubot_common::simulation_strategy_<ContainerAllocator> const>
  : TrueType
  { };

template <class ContainerAllocator>
struct HasHeader< ::nubot_common::simulation_strategy_<ContainerAllocator> >
  : FalseType
  { };

template <class ContainerAllocator>
struct HasHeader< ::nubot_common::simulation_strategy_<ContainerAllocator> const>
  : FalseType
  { };


template<class ContainerAllocator>
struct MD5Sum< ::nubot_common::simulation_strategy_<ContainerAllocator> >
{
  static const char* value()
  {
    return "1d84999556ec502fdeaed67902dd635f";
  }

  static const char* value(const ::nubot_common::simulation_strategy_<ContainerAllocator>&) { return value(); }
  static const uint64_t static_value1 = 0x1d84999556ec502fULL;
  static const uint64_t static_value2 = 0xdeaed67902dd635fULL;
};

template<class ContainerAllocator>
struct DataType< ::nubot_common::simulation_strategy_<ContainerAllocator> >
{
  static const char* value()
  {
    return "nubot_common/simulation_strategy";
  }

  static const char* value(const ::nubot_common::simulation_strategy_<ContainerAllocator>&) { return value(); }
};

template<class ContainerAllocator>
struct Definition< ::nubot_common::simulation_strategy_<ContainerAllocator> >
{
  static const char* value()
  {
    return "StrategyInfo[] strategy_msgs\n\
\n\
================================================================================\n\
MSG: nubot_common/StrategyInfo\n\
Header   header\n\
int32    AgentID\n\
int32    targetNum1\n\
int32    targetNum2\n\
int32    targetNum3\n\
int32    targetNum4\n\
int32    staticpassNum\n\
int32    staticcatchNum\n\
uint32   role\n\
uint32   action\n\
bool     is_dribble\n\
bool     is_kickoff\n\
float32  role_time\n\
PassCommands  pass_cmd\n\
\n\
\n\
\n\
\n\
================================================================================\n\
MSG: std_msgs/Header\n\
# Standard metadata for higher-level stamped data types.\n\
# This is generally used to communicate timestamped data \n\
# in a particular coordinate frame.\n\
# \n\
# sequence ID: consecutively increasing ID \n\
uint32 seq\n\
#Two-integer timestamp that is expressed as:\n\
# * stamp.sec: seconds (stamp_secs) since epoch (in Python the variable is called 'secs')\n\
# * stamp.nsec: nanoseconds since stamp_secs (in Python the variable is called 'nsecs')\n\
# time-handling sugar is provided by the client library\n\
time stamp\n\
#Frame this data is associated with\n\
# 0: no frame\n\
# 1: global frame\n\
string frame_id\n\
\n\
================================================================================\n\
MSG: nubot_common/PassCommands\n\
uint32  pass_id\n\
uint32  catch_id\n\
Point2d pass_pt\n\
Point2d catch_pt\n\
bool    is_passout\n\
bool    is_dynamic_pass\n\
bool    is_static_pass\n\
bool    is_valid\n\
 \n\
\n\
================================================================================\n\
MSG: nubot_common/Point2d\n\
float32 x\n\
float32 y\n\
";
  }

  static const char* value(const ::nubot_common::simulation_strategy_<ContainerAllocator>&) { return value(); }
};

} // namespace message_traits
} // namespace ros

namespace ros
{
namespace serialization
{

  template<class ContainerAllocator> struct Serializer< ::nubot_common::simulation_strategy_<ContainerAllocator> >
  {
    template<typename Stream, typename T> inline static void allInOne(Stream& stream, T m)
    {
      stream.next(m.strategy_msgs);
    }

    ROS_DECLARE_ALLINONE_SERIALIZER
  }; // struct simulation_strategy_

} // namespace serialization
} // namespace ros

namespace ros
{
namespace message_operations
{

template<class ContainerAllocator>
struct Printer< ::nubot_common::simulation_strategy_<ContainerAllocator> >
{
  template<typename Stream> static void stream(Stream& s, const std::string& indent, const ::nubot_common::simulation_strategy_<ContainerAllocator>& v)
  {
    s << indent << "strategy_msgs[]" << std::endl;
    for (size_t i = 0; i < v.strategy_msgs.size(); ++i)
    {
      s << indent << "  strategy_msgs[" << i << "]: ";
      s << std::endl;
      s << indent;
      Printer< ::nubot_common::StrategyInfo_<ContainerAllocator> >::stream(s, indent + "    ", v.strategy_msgs[i]);
    }
  }
};

} // namespace message_operations
} // namespace ros

#endif // NUBOT_COMMON_MESSAGE_SIMULATION_STRATEGY_H