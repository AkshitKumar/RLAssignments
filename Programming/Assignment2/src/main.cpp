/* -.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.

 * File Name : main.cpp

 * Purpose : Herd Management Assignment

 * Creation Date : 02-10-2013

 * Last Modified : Mon 07 Oct 2013 05:48:10 AM IST

 * Created By : npsabari

 _._._._._._._._._._._._._._._._._._._._._.*/

#include "header.h"
#include "parameter.h"
#include "state.h"
#include "afterstate.h"
#include "action.h"
#include "pre_compute.h"
#include "aux_methods.h"

void policy_iteration() {
  /**
   * Initialiazation
   * State values are initially set to 0
   * Initial policy sells all cows for each state
   */
  double state_value[MAX_STATE_NUMBER];
  vector<action*> policy;
  CLR(state_value);

  policy.resize(MAX_STATE_NUMBER);

  REP(i, MAX_STATE_NUMBER) {
    ppi split = get_split(rev_naming[i]);
    policy[i] = new action(split.ff.ff, split.ff.ss, split.ss);
  }

  int iter = 0;

  int sweep_count = 0;
  while(true) { 
    ++iter;

    // Policy Evaluation
    int eval_count = 0;
    double delta;
    do {
      ++eval_count;
      ++sweep_count;
      delta = 0;
      double prev_value, new_value;
      REP(i, MAX_STATE_NUMBER) {
        prev_value = state_value[i];
        new_value = 0.0;
        ppi current_split = get_split(rev_naming[i]);

        state* current_afterstate = 
          new afterstate(
              current_split.ff.ff - policy[i]->num_young, 
              current_split.ff.ss - policy[i]->num_breedable,
              current_split.ss - policy[i]->num_old
              );
        int repr = current_afterstate->get_state_rep();

        double reward = current_afterstate->num_young * expected_utility[0] + policy[i]->num_young * expected_payoff[0]
          + current_afterstate->num_breedable * expected_utility[1] + policy[i]->num_breedable * expected_payoff[1]
          + current_afterstate->num_old * expected_utility[2] + policy[i]->num_old * expected_payoff[2];

        //Iterating over all states from the given afterstate

        REP(m, MAX_STATE_NUMBER) {
          new_value += afterstate_to_state[repr][m] * ( reward + GAMMA * state_value[m] );
        }
        state_value[i] = new_value;
        delta = max(delta, abs(new_value - prev_value));
      }
      cout<<eval_count<<" iterations done in eval"<<endl;
      if (sweep_count == 1) {
        stringstream ss;
        ss <<"../outfile/policy_"<<GAMMA<<"_1";
        ofstream outfile(ss.str().c_str());
        REP(i, MAX_STATE_NUMBER) {
          outfile<<state_value[i]<<endl;
        }
        outfile.close();
      }
      if (sweep_count == 10) {
        stringstream ss;
        ss <<"../outfile/policy_"<<GAMMA<<"_10";
        ofstream outfile(ss.str().c_str());
        REP(i, MAX_STATE_NUMBER) {
          outfile<<state_value[i]<<endl;
        }
        outfile.close();
      }

    } while( delta > CONVERGENCE_EPS);

    // Policy Improvement
    bool policy_stable = true; 
    double new_value;
    // Iteration over all states
    REP(i, MAX_STATE_NUMBER) {
      ppi current_split = get_split(rev_naming[i]);
      action* optimal_action = new action(policy[i]);
      double max_value = -INF;

      // Iterating over all after states or actions possible
      // Here indices represents number of cows present in the next afterstate
      REP(j, current_split.ff.ff+1) {
        REP(k, current_split.ff.ss+1) {
          REP(l, current_split.ss+1) {
            state* current_afterstate = new afterstate(j, k, l);
            int repr = current_afterstate->get_state_rep();

            action* current_action = new action(current_split.ff.ff-j, current_split.ff.ss-k, current_split.ss-l);
            double reward = current_afterstate->num_young * expected_utility[0] + current_action->num_young * expected_payoff[0]
              + current_afterstate->num_breedable * expected_utility[1] + current_action->num_breedable * expected_payoff[1]
              + current_afterstate->num_old * expected_utility[2] + current_action->num_old * expected_payoff[2];

            new_value = 0.0;
            REP(m, MAX_STATE_NUMBER) {
              new_value += afterstate_to_state[repr][m] * ( reward + GAMMA * state_value[m] );
            }
            if (new_value > max_value) {
              optimal_action = new action(current_action);
              max_value = new_value;
            }
          }
        }
      }

      if (policy[i]->equals(optimal_action)) {
        continue;
      } else {
        policy_stable = false;
        policy[i] = new action(optimal_action);
      }
    }

    if (policy_stable) {
      cout<<"Policy Iteration converged in "<<iter<<" iterations"<<endl;

      stringstream ss;
      ss <<"../outfile/policy_"<<GAMMA;
      ofstream outfile(ss.str().c_str());
      REP(i, MAX_STATE_NUMBER) {
        outfile<<state_value[i]<<endl;
      }
      outfile.close();
      action* t = policy[compress_naming[TEST_INPUT_1]];
      cout<<"optimal action for TEST 1 ";
      cout<<t->num_young<<" "<<t->num_breedable<<" "<<t->num_old<<endl;
      t = policy[compress_naming[TEST_INPUT_2]];
      cout<<"optimal action for TEST 2 ";
      cout<<t->num_young<<" "<<t->num_breedable<<" "<<t->num_old<<endl;
      t = policy[compress_naming[TEST_INPUT_3]];
      cout<<"optimal action for TEST 3 ";
      cout<<t->num_young<<" "<<t->num_breedable<<" "<<t->num_old<<endl;

      break;
    } else {
      cout<<iter<<" policy iterations done"<<endl;
    }
  }
}

void value_iteration() {
  /**
   * Initialiazation
   * State values are initially set to 0
   */
  double state_value[MAX_STATE_NUMBER];
  CLR(state_value);

  double delta;

  int iter = 0;
  do {
    ++iter;
    delta = 0.0;
    double prev_value, new_value;
    REP(i, MAX_STATE_NUMBER) {
      prev_value = state_value[i];
      ppi current_split = get_split(rev_naming[i]);

      double max_value = -INF;

      // Iterating over all after states or actions possible
      // Here indices represents number of cows present in the next afterstate
      REP(j, current_split.ff.ff+1) {
        REP(k, current_split.ff.ss+1) {
          REP(l, current_split.ss+1) {

            state* current_afterstate = new state(j, k, l);
            int repr = current_afterstate->get_state_rep();

            action* current_action = new action(current_split.ff.ff-j, current_split.ff.ss-k, current_split.ss-l);
            double reward = current_afterstate->num_young * expected_utility[0] + current_action->num_young * expected_payoff[0]
              + current_afterstate->num_breedable * expected_utility[1] + current_action->num_breedable * expected_payoff[1]
              + current_afterstate->num_old * expected_utility[2] + current_action->num_old * expected_payoff[2];

            new_value = 0.0;
            REP(m, MAX_STATE_NUMBER) {
              new_value += afterstate_to_state[repr][m] * ( reward + GAMMA * state_value[m] );
            }
            max_value = max(max_value, new_value);
          }
        }
      }
      state_value[i] = max_value;
      delta = max(delta, abs(state_value[i] - prev_value));
    }
    cout<<iter<<" value iterations done"<<endl;
    if (iter == 1) {
      stringstream ss;
      ss <<"../outfile/value_"<<GAMMA<<"_1";
      ofstream outfile(ss.str().c_str());
      REP(i, MAX_STATE_NUMBER) {
        outfile<<state_value[i]<<endl;
      }
      outfile.close();
    }
    if (iter == 10) {
      stringstream ss;
      ss <<"../outfile/value_"<<GAMMA<<"_10";
      ofstream outfile(ss.str().c_str());
      REP(i, MAX_STATE_NUMBER) {
        outfile<<state_value[i]<<endl;
      }
      outfile.close();
    }
  } while( delta > CONVERGENCE_EPS);


  // Getting the optimal policy for each state

  vector<action*> policy;
  policy.resize(MAX_STATE_NUMBER);

  double new_value;
  // Iteration over all states
  REP(i, MAX_STATE_NUMBER) {
    ppi current_split = get_split(rev_naming[i]);
    action* optimal_action = new action(0, 0, 0);
    double max_value = -INF;

    // Iterating over all after states or actions possible
    // Here indices represents number of cows present in the next afterstate
    REP(j, current_split.ff.ff+1) {
      REP(k, current_split.ff.ss+1) {
        REP(l, current_split.ss+1) {
          state* current_afterstate = new afterstate(j, k, l);
          int repr = current_afterstate->get_state_rep();

          action* current_action = new action(current_split.ff.ff-j, current_split.ff.ss-k, current_split.ss-l);
          double reward = current_afterstate->num_young * expected_utility[0] + current_action->num_young * expected_payoff[0]
            + current_afterstate->num_breedable * expected_utility[1] + current_action->num_breedable * expected_payoff[1]
            + current_afterstate->num_old * expected_utility[2] + current_action->num_old * expected_payoff[2];

          new_value = 0.0;
          REP(m, MAX_STATE_NUMBER) {
            new_value += afterstate_to_state[repr][m] * ( reward + GAMMA * state_value[m] );
          }
          if (new_value > max_value) {
            optimal_action = new action(current_action);
            max_value = new_value;
          }
        }
      }
    }
    policy[i] = new action(optimal_action);
  }

  stringstream ss;
  ss <<"../outfile/value_"<<GAMMA;
  ofstream outfile(ss.str().c_str());
  REP(i, MAX_STATE_NUMBER) {
    outfile<<state_value[i]<<endl;
  }
  outfile.close();
  action* t = policy[compress_naming[TEST_INPUT_1]];
  cout<<"optimal action for TEST 1 ";
  cout<<t->num_young<<" "<<t->num_breedable<<" "<<t->num_old<<endl;
  t = policy[compress_naming[TEST_INPUT_2]];
  cout<<"optimal action for TEST 2 ";
  cout<<t->num_young<<" "<<t->num_breedable<<" "<<t->num_old<<endl;
  t = policy[compress_naming[TEST_INPUT_3]];
  cout<<"optimal action for TEST 3 ";
  cout<<t->num_young<<" "<<t->num_breedable<<" "<<t->num_old<<endl;
}


int main(int argc, char** argv) {

  pre_compute_factorial();
  pre_compute_mapping();
  cout<<"pre computation done"<<endl;

  generate_prob_map();
  cout<<"Generation of probability matrices done"<<endl;

  validation();
  cout<<"validation of probability matrices done"<<endl;

  policy_iteration();

  value_iteration();

  return 0;
}
