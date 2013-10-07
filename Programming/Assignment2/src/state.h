#ifndef __STATE_H
#define __STATE_H

#include "parameter.h"

class state {
  public:
    int num_young;
    int num_breedable;
    int num_old;
    int total_cows;
    state();
    state(int, int, int);
    int get_state_rep();
};
#endif // __STATE_H_
