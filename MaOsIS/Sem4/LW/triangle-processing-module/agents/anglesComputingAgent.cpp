#include <unordered_set>
#include <vector>

#include "sc-agents-common/utils/IteratorUtils.hpp"
#include "sc-agents-common/utils/AgentUtils.hpp"
#include "sc-agents-common/utils/CommonUtils.hpp"
#include "sc-agents-common/keynodes/coreKeynodes.hpp"
#include <sc-memory/sc_link.hpp>
#include <sc-memory/sc_memory.hpp>

#include "anglesComputingAgent.hpp"

using namespace std;
using namespace utils;

using Isomorphism = unordered_map<const ScAddr, const ScAddr, ScAddrHashFunc<uint32_t>>; 

namespace triangleProcessingModuleNamespace
{

SC_AGENT_IMPLEMENTATION(anglesComputingAgent)
{
  ScAddr actionAddr = otherAddr;
  if (checkActionClass(actionAddr) == SC_FALSE)
    return SC_RESULT_OK;

  SC_LOG_ERROR("AnglesComputingAgent started");

  try
  {
    ScAddr inputStructNode =
      utils::IteratorUtils::getAnyByOutRelation(&m_memoryCtx, actionAddr, Keynodes::rrel_1);

    ScAddr inputTriangleNode =
      utils::IteratorUtils::getAnyByOutRelation(&m_memoryCtx, inputStructNode, Keynodes::rrel_main_key_sc_element);

    SC_CHECK_PARAM(inputTriangleNode, "No key element in input struct");

    // Extract all angles of triangle
    ScAddrVector anglesNodesToProcess;

    ScIterator5Ptr anglesIterator = m_memoryCtx.Iterator5(
        inputTriangleNode,
        ScType::EdgeDCommonConst,
        ScType::Node,
        ScType::EdgeAccessConstPosPerm,
        Keynodes::nrel_angle);

    while (anglesIterator->Next())
    {
      anglesNodesToProcess.push_back(anglesIterator->Get(2));
    }

    if(anglesNodesToProcess.size() != 3) {
      printf("Actual angles count: %ld", anglesNodesToProcess.size());
      SC_LOG_ERROR("Found incorrect number of angles (should be 3)");
      utils::AgentUtils::finishAgentWork(&m_memoryCtx, actionAddr, false);
      return SC_RESULT_ERROR;
    }

    // Find angle with known value
    // Extract value from known one

    ScAddr knownAngleNode;
    ScAddr knownAngleValueNode;

    for (const auto& angleNode : anglesNodesToProcess)
    {
      ScIterator5Ptr knownValueIterator = m_memoryCtx.Iterator5(
          angleNode,
          ScType::EdgeDCommonConst,
          ScType::Node,
          ScType::EdgeAccessConstPosPerm,
          Keynodes::nrel_value);

      if (knownValueIterator->Next())
      {
        knownAngleNode = knownValueIterator->Get(0);
        knownAngleValueNode = knownValueIterator->Get(2);
        break;
      }
    }

    SC_CHECK_PARAM(knownAngleNode, "No angle with known value found");

    ScAddrVector::iterator position = std::find(anglesNodesToProcess.begin(), 
                                                anglesNodesToProcess.end(), 
                                                knownAngleNode);
    if (position != anglesNodesToProcess.end())
        anglesNodesToProcess.erase(position);

    if(anglesNodesToProcess.size() != 2) {
      SC_LOG_ERROR("Incorrect angles number encountered");
      utils::AgentUtils::finishAgentWork(&m_memoryCtx, actionAddr, false);
      return SC_RESULT_ERROR;
    }

    // Compute angles (and create map*)

    // ! Links won't work !
    //
    // ScLink link(m_memoryCtx, knownAngleValueNode);
    // string content = link.GetAsString();
    // printf("Link content: %s\n", content.c_str());
    string content = m_memoryCtx.HelperGetSystemIdtf(knownAngleValueNode);
    int knownAngleValue = stoi(content);
    int thirdAngleValue = 180 - (knownAngleValue * 2);

    // Check for equality

    ScIterator5Ptr equalityIterator = m_memoryCtx.Iterator5(
        knownAngleNode,
        ScType::EdgeDCommonConst,
        ScType::Node,
        ScType::EdgeAccessConstPosPerm,
        Keynodes::nrel_equal);

    // Generate value for equal angle
    if (equalityIterator->Next())
    {
      // ! Links won't work !
      //
      ScAddr equalAngle = equalityIterator->Get(2);

      // ScAddr angleValueNode = m_memoryCtx.CreateNode(ScType::NodeConst);
      // ScLink link2(m_memoryCtx, angleValueNode);
      // link2.Set(knownAngleValue);
      // ScAddr valueRelationEdge = m_memoryCtx.CreateEdge(ScType::EdgeDCommonConst, equalAngle, angleValueNode);
      // m_memoryCtx.CreateEdge(ScType::EdgeAccessConstPosPerm, Keynodes::nrel_value, valueRelationEdge);
      printf("Second angle value: %d\n", knownAngleValue);


      // remove from list to process
      ScAddrVector::iterator position2 = std::find(anglesNodesToProcess.begin(), 
                                                anglesNodesToProcess.end(), 
                                                equalAngle);
      if (position2 != anglesNodesToProcess.end())
          anglesNodesToProcess.erase(position2);
    }
    else 
    {
      SC_LOG_ERROR("Not enough data to calculate angles values");
      utils::AgentUtils::finishAgentWork(&m_memoryCtx, actionAddr, false);
      return SC_RESULT_ERROR;
    }

    // Generate value for third angle

    // ! Links won't work !
    //
    // ScAddr thirdAngle = anglesNodesToProcess[0];
    // ScAddr angleValueNode = m_memoryCtx.CreateNode(ScType::NodeConst);
    // ScLink link3(m_memoryCtx, angleValueNode);
    // link3.Set(thirdAngleValue);
    // ScAddr valueRelationEdge = m_memoryCtx.CreateEdge(ScType::EdgeDCommonConst, thirdAngle, angleValueNode);
    // m_memoryCtx.CreateEdge(ScType::EdgeAccessConstPosPerm, Keynodes::nrel_value, valueRelationEdge);

    printf("Third angle value: %d\n", thirdAngleValue);

    if(knownAngleValue == 90
      || thirdAngleValue == 90)
    {
      SC_LOG_INFO("Triangle is rectangular");

      // todo: remove if links work
      m_memoryCtx.CreateEdge(ScType::EdgeAccessConstPosPerm, Keynodes::concept_rectangular_triangle, inputTriangleNode);
    }
    else 
    {
      SC_LOG_INFO("Triangle is NOT rectangular");  
    // todo: remove if links work
      m_memoryCtx.CreateEdge(ScType::EdgeAccessConstNegPerm, Keynodes::concept_rectangular_triangle, inputTriangleNode);
    }
  }
  catch (utils::ScException const & exception)
  {
    SC_LOG_ERROR(exception.Message());
    utils::AgentUtils::finishAgentWork(&m_memoryCtx, actionAddr, false);
    return SC_RESULT_ERROR;
  }
  catch (exception & ex)
  {
    SC_LOG_ERROR(ex.what());
    utils::AgentUtils::finishAgentWork(&m_memoryCtx, actionAddr, false);
    return SC_RESULT_ERROR;
  }

  SC_LOG_ERROR("AnglesComputingAgent finished");
  utils::AgentUtils::finishAgentWork(&m_memoryCtx, actionAddr, true);
  return SC_RESULT_OK;
}


bool anglesComputingAgent::checkActionClass(ScAddr const & actionAddr)
{
  return m_memoryCtx.HelperCheckEdge(
      Keynodes::action_compute_triangle_angles, actionAddr, ScType::EdgeAccessConstPosPerm);
}

}