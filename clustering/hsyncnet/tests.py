import unittest;

from nnet import *;

from support import read_sample;

from clustering.hsyncnet import hsyncnet;

from samples.definitions import SIMPLE_SAMPLES;

class Test(unittest.TestCase):
    def templateClustering(self, path, number_clusters, expected_length_clusters):
        result_testing = False;
        
        # If phases crosses each other because of random part of the network then we should try again.
        for attempt in range(0, 3, 1):
            sample = read_sample(path);
            network = hsyncnet(sample, initial_type.EQUIPARTITION); # EQUIPARTITION - makes test more stable.
            
            (t, d) = network.process(number_clusters, order = 0.998, collect_dynamic = True);
            clusters = network.get_clusters();
            
            if (sum([len(cluster) for cluster in clusters]) != sum(expected_length_clusters)):
                continue;
            
            if (sorted([len(cluster) for cluster in clusters]) != expected_length_clusters):
                if (sorted([len(cluster) for cluster in clusters]) != expected_length_clusters):
                    continue;
            
            # Unit-test is passed
            result_testing = True;
            break;
        
        assert result_testing;
        
    
    def testClusteringSampleSimple1(self):
        self.templateClustering(SIMPLE_SAMPLES.SAMPLE_SIMPLE1, 2, [5, 5]);
        
    def testClusteringOneAllocationSampleSimple1(self):
        self.templateClustering(SIMPLE_SAMPLES.SAMPLE_SIMPLE1, 1, [10]);

    def testClusteringSampleSimple2(self):
        self.templateClustering(SIMPLE_SAMPLES.SAMPLE_SIMPLE2, 3, [5, 8, 10]);
        
    def testClusteringOneAllocationSampleSimple2(self):
        self.templateClustering(SIMPLE_SAMPLES.SAMPLE_SIMPLE2, 1, [23]);    


if __name__ == "__main__":
    unittest.main()