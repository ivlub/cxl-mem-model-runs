
corecount = 1  # As we only can trace one MPI rank at a time, we can leave corecount to 1
clock = "1.7GHz"

# Ariel params
ariel_params = {
    "verbose": "1",
    #"maxcorequeue": "256",
    #"maxissuepercycle": "2",
    #"pipetimeout": "0",
    "corecount": str(corecount),
    "clock": clock,
    "executable": args.binary,
    "appargcount": len(args.args),
    "arielmode": 0, # set to 1 to trace entire program (default), set to 0 to delay tracing until ariel_enable() call.
    "arielinterceptcalls": "0",  # Do not intercept malloc/free
    "launchparamcount": 1,
    "launchparam0": "-ifeellucky",  # For Pin2.14 on newer hardware
    "mpilauncher": "build/mpilauncher",
    "mpimode": 1,
    "mpiranks": args.nranks,
    "mpitracerank": args.tracerank,
}

# Add target binary arguments to ariel
for i, apparg in enumerate(args.args):
    ariel_params["apparg" + str(i)] = apparg

# Tracer Params
tracer_params = {
    "clock": clock,
    "mpi_trace_out": args.out_dir + "/data/mpi_traces.csv",
    "mem_trace_out": args.out_dir + "/data/samples.csv",
    "debug": "8",
    "corecount": str(corecount)
}

# Default parameters for L1
l1_params = {
    "cache_frequency": clock,
    "access_latency_cycles": 4,
    "cache_size": "32KB",
    "associativity": 8,
    "cache_line_size": 64,
    "L1": 1,
    "verbose": 1,
}

l1_prefetcher_params = {}

# Default parameters for L2
l2_params = {
    "cache_frequency": clock,
    "access_latency_cycles": 12,
    "cache_size": "1024KB",
    "associativity": 16,
    "cache_line_size": 64,
    "verbose": 1,
}

l2_prefetcher_params = {}

# Default parameters for L3
l3_params = {
    "cache_frequency": clock,
    "access_latency_cycles": 17,
    "cache_size": "11MB",
    "associativity": 16, # Should be 11
    "cache_line_size": 64,
    "verbose": 1,
}

l3_prefetcher_params = {}

# Memory controller params
memctrl_params = {
    "clock": clock
}

# Memory params
mem_params = {
    "access_time": "110ns",
    "mem_size": "78GB"
}

# ======================================================================================================================
