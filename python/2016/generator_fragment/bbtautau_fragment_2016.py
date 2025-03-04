# Request made with AutoClone script: /afs/cern.ch/work/a/agapitos/public/MC4/AutoClone/Radion_hh_htatahbb_incl_narrow.py 

import FWCore.ParameterSet.Config as cms

externalLHEProducer = cms.EDProducer("ExternalLHEProducer",
                                     args = cms.vstring('/cvmfs/cms.cern.ch/phys_generator/gridpacks/2017/13TeV/madgraph/V5_2.6.5/exo_diboson/Spin-0/Radion_hh_htatahbb_incl_narrow/Radion_hh_htatahbb_incl_narrow_M1000_slc7_amd64_gcc700_CMSSW_10_6_19_tarball.tar.xz'),
                                     nEvents = cms.untracked.uint32(5000),
                                     numberOfParameters = cms.uint32(1),
                                     outputFile = cms.string('cmsgrid_final.lhe'),
                                     scriptName = cms.FileInPath('GeneratorInterface/LHEInterface/data/run_generic_tarball_cvmfs.sh')
)
# Link to cards: https://github.com/aloeliger/genproductions/tree/master/bin/MadGraph5_aMCatNLO/cards/production/2017/13TeV/exo_diboson/Spin-0/Radion_hh_htatahbb_incl_narrow

import FWCore.ParameterSet.Config as cms

from Configuration.Generator.Pythia8CommonSettings_cfi import *
from Configuration.Generator.MCTunes2017.PythiaCP5Settings_cfi import *
from Configuration.Generator.PSweightsPythia.PythiaPSweightsSettings_cfi import *

generator = cms.EDFilter("Pythia8HadronizerFilter",
                         maxEventsToPrint = cms.untracked.int32(1),
                         pythiaPylistVerbosity = cms.untracked.int32(1),
                         filterEfficiency = cms.untracked.double(1.0),
                         pythiaHepMCVerbosity = cms.untracked.bool(False),
                         comEnergy = cms.double(13000.),
                         PythiaParameters = cms.PSet(
       pythia8CommonSettingsBlock,
        pythia8CP5SettingsBlock,
        pythia8PSweightsSettingsBlock,
                             parameterSets = cms.vstring('pythia8CommonSettings',
                                   'pythia8CP5Settings',
                                    'pythia8PSweightsSettings',)
    )
)
