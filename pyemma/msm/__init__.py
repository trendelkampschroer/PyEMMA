# Copyright (c) 2015, 2014 Computational Molecular Biology Group, Free University
# Berlin, 14195 Berlin, Germany.
# All rights reserved.
#
# Redistribution and use in source and binary forms, with or without modification,
# are permitted provided that the following conditions are met:
#
#  * Redistributions of source code must retain the above copyright notice, this
# list of conditions and the following disclaimer.
#  * Redistributions in binary form must reproduce the above copyright notice,
# this list of conditions and the following disclaimer in the documentation and/or
# other materials provided with the distribution.
#
# THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS ``AS IS''
# AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE
# IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE
# DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT HOLDER OR CONTRIBUTORS BE LIABLE FOR
# ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES
# (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES;
# LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON
# ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT
# (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE OF THIS
# SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.

r"""

.. currentmodule:: pyemma.msm

User API
========
For most users, the following high-level functions provide are sufficient to estimate msm models from data.
Expert users may want to construct Estimators or Models (see below) directly.

.. autosummary::
   :toctree: generated/

   markov_model
   timescales_msm
   its
   estimate_markov_model
   bayesian_markov_model
   tpt
   timescales_hmsm
   estimate_hidden_markov_model
   bayesian_hidden_markov_model


**Estimators** to generate models from data. If you are not an expert user,
use the API functions above.

.. autosummary::
   :toctree: generated/

   ImpliedTimescales
   MaximumLikelihoodMSM
   BayesianMSM
   MaximumLikelihoodHMSM
   BayesianHMSM


**Models** of the kinetics or stationary properties of the data. 
If you are not an expert user, use API functions above.

.. autosummary::
   :toctree: generated/

   MSM
   EstimatedMSM
   SampledMSM
   HMSM
   EstimatedHMSM
   SampledHMSM
   ReactiveFlux


MSM functions (low-level API)
=============================
Low-level functions for estimation and analysis of transition matrices and io.

.. toctree::
   :maxdepth: 1

   msm.dtraj
   msm.generation
   msm.estimation
   msm.analysis
   msm.flux

"""
from __future__ import absolute_import, print_function

#####################################################
# Low-level MSM functions (imported from msmtools)
# backward compatibility to PyEMMA 1.2.x
from msmtools import analysis, estimation, generation, dtraj, flux
from msmtools.flux import ReactiveFlux
io = dtraj

#####################################################
# Estimators and models
from .estimators import MaximumLikelihoodMSM, BayesianMSM
from .estimators import MaximumLikelihoodHMSM, BayesianHMSM
from .estimators import ImpliedTimescales
from .estimators import EstimatedMSM, EstimatedHMSM

from .models import MSM, HMSM, SampledMSM, SampledHMSM

# high-level api
from .api import *
