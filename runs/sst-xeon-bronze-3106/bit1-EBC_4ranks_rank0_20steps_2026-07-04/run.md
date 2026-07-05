# BIT1 EBC — 4 ranks, 20 steps — sst_xeon_bronze_3106
- Simulated machine: Intel Xeon Bronze 3106 (8c @ 1.7 GHz), see config/sst_hw.py
  (clock 1.7GHz; L1 4cyc/32KB/8w; L2 12cyc/1MB/16w; L3 17cyc/11MB/16w; DRAM 110ns/78GB)
- Physical host: bg1 / i10se26 (AMD EPYC 9754)
- Deck: bit_EBC_ivan_20steps.inp ; ranks: 4 ; traced rank: 0 ; steps: 20
- SST cache policy: l1_no_pf_l2_stride_l3_stride (config/sst_cache.json, index 0)
- Date: 2026-07-04
- SST wall-clock: 143m05s ; simulated time: 4.71 s ; ~1820x slowdown
- Native EPYC step: 0.054 s ; simulated Bronze-3106 step: 0.169 s

# Results
- tag 15/23 (field solve / density halo): CXL slightly worse
- tag 19 (particle exchange): CXL -2.02ms

