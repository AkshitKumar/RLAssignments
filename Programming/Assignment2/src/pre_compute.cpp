/* -.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.

* File Name : pre_compute.cpp

* Purpose : Herd Management Assignment

* Creation Date : 06-10-2013

* Last Modified : Sun 06 Oct 2013 04:46:06 AM IST

* Created By : npsabari

_._._._._._._._._._._._._._._._._._._._._.*/

#include "pre_compute.h"

double evolve_prob[MAX_STATE_NUMBER][MAX_STATE_NUMBER];
double reproduction_prob[MAX_STATE_NUMBER][MAX_STATE_NUMBER];
double afterstate_to_state[MAX_STATE_NUMBER][MAX_STATE_NUMBER];

double expected_payoff[NUM_COW_TYPES] = {2, 6, 4};
double expected_utility[NUM_COW_TYPES] = {0.3, 0.4, 0.2};

double transition_probability[NUM_COW_TYPES][NUM_COW_TYPES] = {
  {0.9 , 0.1 , 0.0 },
  {0.0 , 0.75, 0.25},
  {0.0 , 0.15, 0.85}
};

double offspring_probability[NUM_COW_TYPES][MAX_OFFSPRINGS+1] = {
  {1.0 , 0.0 , 0.0 },
  {0.05, 0.8 , 0.15},
  {1.0 , 0.0 , 0.0 }
};

map<int, int> compress_naming;
map<int, int> rev_naming;

ll factorial[NUM_COWS+1];

void pre_compute_factorial() {
  factorial[0] = factorial[1] = 1;
  FORab(i, 2, NUM_COWS) {
    factorial[i] = i * factorial[i-1];
  }
}

void pre_compute_mapping() {
  int counter = 0;
  REP(i, NUM_COWS+1) {
    REP(j, NUM_COWS+1-i) {
      REP(k, NUM_COWS+1-j-i) {
        compress_naming[169*i + 13*j + k] = counter;
        rev_naming[counter] = 169*i + 13*j + k;
        ++counter;
      }
    }
  }
}

void get_evolve_prob(state* current_afterstate) {
  /**
   * Possible Transitions from the current afterstate
   * Max number of each cow type possible after the transitions
   * Young - current_afterstate->num_young
   * Breedable - current_afterstate->num_young + current_afterstate->num_breedable + current_afterstate->num_old ( so wierd !! )
   * Old - current_afterstate->num_breedable + current_afterstate->num_old
   */
  
  double young_trans, breedable_trans, old_trans;
  int repr;

  // Each Index represents the number of cows of a particular type transitioning
  REP(i, current_afterstate->num_young+1) {
    young_trans = get_power(transition_probability[0][1], i)
      * get_power(transition_probability[0][0], current_afterstate->num_young - i)
      * getnCr(current_afterstate->num_young, i);

    REP(j, current_afterstate->num_breedable+1) {
      breedable_trans = get_power(transition_probability[1][2], j)
        * get_power(transition_probability[1][1], current_afterstate->num_breedable - j)
        * getnCr(current_afterstate->num_breedable, j);

      REP(k, current_afterstate->num_old+1) {
        old_trans = get_power(transition_probability[2][1], k)
          * get_power(transition_probability[2][2], current_afterstate->num_old - k)
          * getnCr(current_afterstate->num_old, k);

        repr = compress_naming[(current_afterstate->num_young-i)*169 
          + (current_afterstate->num_breedable-j+i+k)*13
          + (current_afterstate->num_old-k+j)*1];

        evolve_prob[current_afterstate->get_state_rep()][repr] += young_trans*breedable_trans*old_trans;

      }
    }
  }
}

void generate_evolve_prob() {
  REP(i, NUM_COWS+1) {
    REP(j, NUM_COWS-i+1) {
      REP(k, NUM_COWS-i-j+1) {
        state* current_afterstate = new afterstate(i, j, k);
        get_evolve_prob(current_afterstate);      
      }
    }
  }
}

void get_reproduction_prob(state* current_tmp_state) {
  // i -> number of breedables reproducing 1 cows
  // j -> number of breedables reproducing 2 cows

  double zero_offspring, one_offspring, two_offspring;

  int current_num_young;

  REP(i, current_tmp_state->num_breedable+1) {
    one_offspring = get_power(offspring_probability[1][1], i);

    REP(j, current_tmp_state->num_breedable+1-i) {
      two_offspring = get_power(offspring_probability[1][2], j);
      zero_offspring = get_power(offspring_probability[1][0], current_tmp_state->num_breedable - i - j);

      current_num_young = 
        min(
          current_tmp_state->num_young + i + 2*j,
          NUM_COWS - current_tmp_state->num_breedable - current_tmp_state->num_old
        );

      // Using Grouping formula getting the probability
      reproduction_prob
        [current_tmp_state->get_state_rep()]
        [compress_naming[
          current_num_young*169 + current_tmp_state->num_breedable*13 + current_tmp_state->num_old]
        ]
          += factorial[current_tmp_state->num_breedable] / factorial[i] / factorial[j]
          / factorial[current_tmp_state->num_breedable-i-j] 
          * zero_offspring * one_offspring * two_offspring;
      // used '+=' instead of '=' because there can be multiple ways to go from one state to another
    }
  }
}

void generate_reproduction_prob() {
  REP(i, NUM_COWS+1) {
    REP(j, NUM_COWS-i+1) {
      REP(k, NUM_COWS-i-j+1) {
        state* current_tmp_state = new state(i, j, k);
        get_reproduction_prob(current_tmp_state);
      }
    }
  }
}

void generate_prob_map() {
  CLR(evolve_prob);
  CLR(reproduction_prob);
  CLR(afterstate_to_state);
  generate_evolve_prob();
  cout<<"evolution probability calculation done"<<endl;
  generate_reproduction_prob();
  cout<<"reproduction probability calculation done"<<endl;

  REP(i, MAX_STATE_NUMBER) {
    REP(j, MAX_STATE_NUMBER) {
      REP(k, MAX_STATE_NUMBER) {
        afterstate_to_state[i][j] += evolve_prob[i][k] * reproduction_prob[k][j];
      }
    }
  }
}
