# BIT1 EBC — 4 ranks, 20 steps — sst_xeon_bronze_3106 (rank 1, interior)
- Simulated machine: Intel Xeon Bronze 3106 (8c @ 1.7 GHz), see config/sst_hw.py
  (clock 1.7GHz; L1 4cyc/32KB/8w; L2 12cyc/1MB/16w; L3 17cyc/11MB/16w; DRAM 110ns/78GB)
- Physical host: bg1 / i10se26 (AMD EPYC 9754)
- Deck: bit_EBC_ivan_20steps.inp ; ranks: 4 ; traced rank: 1 (interior) ; steps: 20
- SST cache policy: l1_no_pf_l2_stride_l3_stride (config/sst_cache.json, index 0)
- Date: 2026-07-05
- SST wall-clock: not captured ; simulated time: 4.86 s
- NOTE: model needs the SST rank-attribution fix (feat/sst-input) to process rank != 0
  (samples.csv 'pid' col is the Ariel core id = 0, not the MPI rank)

# Results
- Interior rank -> six tags present (both-sided exchange), vs rank 0's three.
  124 Irecv buffers here vs rank 0's 62 (talks to both neighbours).
- tags 13/15 (field solve) + 21/23 (density halo): CXL slightly worse 
- tags 17/19 (particle exchange, both directions): CXL -2ms each. But, this is 0.08% of runtime.
