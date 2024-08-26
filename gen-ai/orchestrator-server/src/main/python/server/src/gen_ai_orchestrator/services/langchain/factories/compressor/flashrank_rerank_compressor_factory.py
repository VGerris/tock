#   Copyright (C) 2023-2024 Credit Mutuel Arkea
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
"""Model for creating FlashrankRerankCompressorFactory"""

from gen_ai_orchestrator.models.compressors.flashrank_rerank.flashrank_rerank_params import \
    FlashrankRerankCompressorParams
from gen_ai_orchestrator.services.langchain.factories.compressor.compressor_factory import LangChainCompressorFactory

from langchain.retrievers.document_compressors import FlashrankRerank


class FlashrankRerankCompressorFactory(LangChainCompressorFactory):
    """A class for LangChain Flashrank Rerank Compressor Factory"""
    param: FlashrankRerankCompressorParams

    def get_compressor(self):
        return FlashrankRerank(
            top_n=self.param.min_score,
            score_threshold=self.param.max_documents,
            model=self.param.model
        )
