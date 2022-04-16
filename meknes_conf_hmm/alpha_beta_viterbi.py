#Forward Algorithm
alpha[[2.16428571e-01 1.36400000e-02 1.42400000e-02]
 [1.95769992e-02 4.62921929e-02 0.00000000e+00]
 [4.24880513e-03 0.00000000e+00 7.85375567e-03]
 [9.76003523e-04 0.00000000e+00 3.12326315e-03]
 [3.29921234e-04 6.47449665e-04 0.00000000e+00]
 [3.20008815e-04 1.60363730e-05 5.13796939e-06]
 [1.37170014e-04 2.66283431e-06 3.30297118e-06]
 [1.16064059e-05 2.54283690e-05 0.00000000e+00]
 [2.40343339e-06 0.00000000e+00 4.51873505e-06]
 [2.79097917e-06 4.61284874e-08 7.44634171e-08]]
 
 #Backward Algorithm
 beta[[1.15016146e-05 1.96386385e-05 1.08442431e-05]
 [7.79366660e-05 2.99360418e-05 8.44869264e-05]
 [2.28668211e-04 9.05609248e-05 2.47016139e-04]
 [7.50866995e-04 1.54509881e-03 6.97578825e-04]
 [3.65329877e-03 2.63537125e-03 3.59649833e-03]
 [8.63440960e-03 6.54014081e-03 8.48657256e-03]
 [2.00995806e-02 3.45288760e-02 1.89425333e-02]
 [1.35055084e-01 5.28569859e-02 1.46092673e-01]
 [4.25017143e-01 3.10388571e-01 4.18274286e-01]
 [1.00000000e+00 1.00000000e+00 1.00000000e+00]]
 
 #Viterbi Algorithm
 viterbi ([0, 0, 2, 2, 1, 0, 0, 0, 2, 0], 1.5974935002286267e-07)
 
 #Baum Welch
 
 baum_welch(n_iteration=1)
 {'A_hat': array([[0.59672972, 0.19376389, 0.20950638],
        [0.61225714, 0.07742379, 0.31031907],
        [0.53655268, 0.2211738 , 0.24227352]]),
 'B_hat': array([[0.60591698, 0.24115553, 0.15292749],
        [0.10326011, 0.89673989, 0.        ],
        [0.05281582, 0.        , 0.94718418]]),
 'Pi_hat': array([0.85496042, 0.09200223, 0.05303735])}

 baum_welch(n_iteration=2)
{'A_hat': array([[0.87748492, 0.01295527, 0.1095598 ],
        [0.91165126, 0.05360651, 0.03474223],
        [0.88492554, 0.01770503, 0.09736943]]),
 'B_hat': array([[0.41014493, 0.34136941, 0.24848565],
        [0.78979552, 0.21020448, 0.        ],
        [0.10654666, 0.        , 0.89345334]]),
 'Pi_hat': array([0.53475317, 0.39416723, 0.0710796 ])}
 
 baum_welch(n_iteration=5)
{'A_hat': array([[8.21783182e-01, 1.45954055e-02, 1.63621412e-01],
        [9.98560495e-01, 1.43171283e-03, 7.79208236e-06],
        [9.15074687e-01, 1.47527742e-02, 7.01725392e-02]]),
 'B_hat': array([[0.35848839, 0.3826689 , 0.2588427 ],
        [0.99881539, 0.00118461, 0.        ],
        [0.29252822, 0.        , 0.70747178]]),
 'Pi_hat': array([0.18747245, 0.66804596, 0.14448159])}
 
 baum_welch(n_iteration=10)
{'A_hat': array([[9.99999987e-001, 6.71847722e-014, 1.31617802e-008],
        [1.00000000e+000, 2.19211172e-115, 7.69527435e-118],
        [1.00000000e+000, 9.01932542e-074, 7.47681502e-070]]),
 'B_hat': array([[3.42803960e-001, 3.28598020e-001, 3.28598020e-001],
        [1.00000000e+000, 9.72262592e-116, 0.00000000e+000],
        [1.00000000e+000, 0.00000000e+000, 9.81666974e-064]]),
 'Pi_hat': array([0.12969602, 0.42578717, 0.44451681])}
 
 baum_welch(n_iteration=50)
{'A_hat': array([[9.99999906e-01, 1.90801523e-13, 9.40088605e-08],
        [1.00000000e+00, 0.00000000e+00, 0.00000000e+00],
        [1.00000000e+00, 0.00000000e+00, 0.00000000e+00]]),
 'B_hat': array([[0.34280391, 0.32859804, 0.32859804],
        [1.        , 0.        , 0.        ],
        [1.        , 0.        , 0.        ]]),
 'Pi_hat': array([0.129696  , 0.42578718, 0.44451682])}
 
 baum_welch(n_iteration=100)
{'A_hat': array([[9.99973281e-01, 3.41971526e-10, 2.67188056e-05],
        [1.00000000e+00, 0.00000000e+00, 0.00000000e+00],
        [1.00000000e+00, 0.00000000e+00, 0.00000000e+00]]),
 'B_hat': array([[0.34278777, 0.32860611, 0.32860611],
        [1.        , 0.        , 0.        ],
        [1.        , 0.        , 0.        ]]),
 'Pi_hat': array([0.12968827, 0.42579096, 0.44452077])}
 
 baum_welch(n_iteration=500)
{'A_hat': array([[9.13783677e-01, 1.74376327e-06, 8.62145789e-02],
        [1.00000000e+00, 0.00000000e+00, 0.00000000e+00],
        [1.00000000e+00, 0.00000000e+00, 0.00000000e+00]]),
 'B_hat': array([[0.28912734, 0.35543633, 0.35543633],
        [1.        , 0.        , 0.        ],
        [1.        , 0.        , 0.        ]]),
 'Pi_hat': array([0.10302077, 0.43883776, 0.45814147])}
 
 baum_welch(n_iteration=1000)
{'A_hat': array([[9.13783677e-01, 2.74981838e-06, 8.62135728e-02],
        [1.00000000e+00, 0.00000000e+00, 0.00000000e+00],
        [1.00000000e+00, 0.00000000e+00, 0.00000000e+00]]),
 'B_hat': array([[0.28912734, 0.35543633, 0.35543633],
        [1.        , 0.        , 0.        ],
        [1.        , 0.        , 0.        ]]),
 'Pi_hat': array([0.10302077, 0.43883776, 0.45814147])}
 
 baum_welch(n_iteration=1500)
{'A_hat': array([[9.13783677e-01, 4.32349122e-06, 8.62119992e-02],
        [1.00000000e+00, 0.00000000e+00, 0.00000000e+00],
        [1.00000000e+00, 0.00000000e+00, 0.00000000e+00]]),
 'B_hat': array([[0.28912734, 0.35543633, 0.35543633],
        [1.        , 0.        , 0.        ],
        [1.        , 0.        , 0.        ]]),
 'Pi_hat': array([0.10302077, 0.43883776, 0.45814147])}

 baum_welch(n_iteration=2000)
{'A_hat': array([[9.13783677e-01, 6.76965149e-06, 8.62095530e-02],
        [1.00000000e+00, 0.00000000e+00, 0.00000000e+00],
        [1.00000000e+00, 0.00000000e+00, 0.00000000e+00]]),
 'B_hat': array([[0.28912734, 0.35543633, 0.35543633],
        [1.        , 0.        , 0.        ],
        [1.        , 0.        , 0.        ]]),
 'Pi_hat': array([0.10302077, 0.43883776, 0.45814147])}
 
 baum_welch(n_iteration=2500)
{'A_hat': array([[9.13783677e-01, 1.05390393e-05, 8.62057836e-02],
        [1.00000000e+00, 0.00000000e+00, 0.00000000e+00],
        [1.00000000e+00, 0.00000000e+00, 0.00000000e+00]]),
 'B_hat': array([[0.28912734, 0.35543633, 0.35543633],
        [1.        , 0.        , 0.        ],
        [1.        , 0.        , 0.        ]]),
 'Pi_hat': array([0.10302077, 0.43883776, 0.45814147])}
 
 baum_welch(n_iteration=5000)
 {'A_hat': array([[9.13783677e-01, 3.74788927e-05, 8.61788438e-02],
        [1.00000000e+00, 0.00000000e+00, 0.00000000e+00],
        [1.00000000e+00, 0.00000000e+00, 0.00000000e+00]]),
 'B_hat': array([[0.28912734, 0.35543633, 0.35543633],
        [1.        , 0.        , 0.        ],
        [1.        , 0.        , 0.        ]]),
 'Pi_hat': array([0.10302077, 0.43883776, 0.45814147])}
 
