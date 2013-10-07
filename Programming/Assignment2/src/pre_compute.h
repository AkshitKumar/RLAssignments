#ifndef __PRE_COMPUTE_H_
#define __PRE_COMPUTE_H_

#include "action.h"
#include "header.h"
#include "parameter.h"
#include "state.h"
#include "afterstate.h"
#include "aux_methods.h"

void pre_compute_factorial();
void pre_compute_mapping(); 

void generate_evolve_prob();
void generate_reproduction_prob();
void generate_prob_map();
#endif // __PRE_COMPUTE_H_
