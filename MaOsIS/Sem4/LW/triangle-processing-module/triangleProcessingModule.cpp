
#include "triangleProcessingModule.hpp"
#include "keynodes/keynodes.hpp"
#include "agents/anglesComputingAgent.hpp"

using namespace triangleProcessingModuleNamespace;

SC_IMPLEMENT_MODULE(triangleProcessingModule)

sc_result triangleProcessingModule::InitializeImpl()
{
  if (!Keynodes::InitGlobal())
    return SC_RESULT_ERROR;

  SC_AGENT_REGISTER(anglesComputingAgent)

  return SC_RESULT_OK;
}

sc_result triangleProcessingModule::ShutdownImpl()
{
  SC_AGENT_UNREGISTER(anglesComputingAgent)

  return SC_RESULT_OK;
}
