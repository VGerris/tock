#   Copyright (C) 2024-2025 Credit Mutuel Arkea
#
#   Licensed under the Apache License, Version 2.0 (the "License");
#   you may not use this file except in compliance with the License.
#   You may obtain a copy of the License at
#
#   http://www.apache.org/licenses/LICENSE-2.0
#
#   Unless required by applicable law or agreed to in writing, software
#   distributed under the License is distributed on an "AS IS" BASIS,
#   WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#   See the License for the specific language governing permissions and
#   limitations under the License.
#
from gen_ai_orchestrator.models.errors.errors_models import ErrorCode


def test_errors_are_documented():
    """Test that a description or error codes is added to the Pydantic schema."""
    first_error_code = ErrorCode.GEN_AI_UNKNOWN_ERROR
    schema = ErrorCode.__get_pydantic_json_schema__(core_schema=None, handler=None)
    assert (
        f'* `{first_error_code.value}`: {first_error_code.name}'
        in schema['description']
    )
