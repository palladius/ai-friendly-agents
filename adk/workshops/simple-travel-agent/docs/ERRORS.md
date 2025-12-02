
# Possible errors

## Tool use with function calling is unsupported

google.genai.errors.ClientError: 400 INVALID_ARGUMENT. {'error': {'code': 400, 'message': 'Tool use with function calling is unsupported', 'status': 'INVALID_ARGUMENT', 'details': [{'@type': 'type.googleapis.com/google.rpc.DebugInfo', 'detail': '[ORIGINAL ERROR] generic::invalid_argument: Tool use with function calling is unsupported [google.rpc.error_details_ext] { message: "Tool use with function calling is unsupported" details { type_url: "type.googleapis.com/language_labs.genai.debug.GeminiApiDebugInfo" value: "\\222\\001\\\\\\n-Tool use with function calling is unsupported\\022+apiserving/util/error_status_utils.cc:109:0" } }'}]}}

This is a known limitation: you either use Tools or GoogleSearch.
