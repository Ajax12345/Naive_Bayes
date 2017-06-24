#include <iostream>
#include <string>
#include <fstream>
#include <vector>
#include <map>
#include <set>
#include <numeric>
#include <cmath>
#include <array>

using namespace std;

struct Classifier
{
  map<int, vector<vector<double> > >final_dictionary;
  map<int, vector<vector<double> > >zipped; //contains ssdev and average for all data
  void classify();
  void calcSSDEV();
  void final_output(array<int, 2>user_input);
  map<int, double>final_dict;

  double output()
  {
    vector<double>vals;
    for (auto i: labels)
    {
      vals.push_back(final_dict[i]);
    }
    double max = 0;
    for (auto i: vals)
    {
      if (i > max)
      {
        max = i;
      }
    }
    double result;
    for (auto i: labels)
    {
      if (final_dict[i] == max)
      {
        result = i;
      }
    }
    return result;
  }
  double functional_density(double x, double o, double u)
  {
    if (o == 0)
    {
      return 1;
    }
    else
    {
      return 1/o*pow(2*3.1415, 0.5)*pow(2.7181, -0.5*pow((x-u)/o, 2));
    }
  }


  void show_stuff();

  set<double>labels;


};





int main()
{

  Classifier predictions;
  predictions.classify();
  predictions.calcSSDEV();
  array<int, 2>the_array = {52, 80};
  //predictions.show_stuff();
  predictions.final_output(the_array);

  cout << predictions.output() << endl;

}

void Classifier::classify()
{
  ifstream input;
  input.open("datafile1.txt");
  int row_counter = 0;

  double file_val;

  input >> file_val;


  vector<double>row;
  while (!input.eof())
  {
    if (row_counter < 2)
    {
      row.push_back(file_val);
      row_counter++;

    }
    else
    {

      labels.insert(file_val);
      final_dictionary[file_val].push_back(row);
      row_counter = 0;
      row.clear();
    }
    input >> file_val;

  }
}


void Classifier::calcSSDEV()
{
  for (auto i:labels)
  {
    vector<vector<double> >data = final_dictionary[i];

    vector<vector<double> >final_calculations;
    for (int b = 0; b<data[0].size(); b++)
    {
      vector<double>rows;
      vector<double>calcs;
      for (auto c: data)
      {
        rows.push_back(c[b]);
      }
      double ave = accumulate(rows.begin(), rows.end(), 0)/rows.size();
      double sum = 0.0;
      for (auto d: rows)
      {
        sum += pow(ave-d, 2);
      }
      double ssdev = pow(sum, 0.5);
      calcs.push_back(ave);
      calcs.push_back(ssdev);
      final_calculations.push_back(calcs);
      //switched.push_back(rows);
      //rows.clear();
    }
    zipped[i] = final_calculations;
  }
}


void Classifier::show_stuff()
{
  for (auto i: labels)
  {
    cout <<i << endl;
    for (auto b:zipped[i])
    {
      for (auto c: b)
      {
        cout << c << endl;
      }
    }
  }
}


void Classifier::final_output(array<int, 2>user_input)
{

  for (auto i:labels)
  {
    final_dict[i] = 1;
  }
  for (auto a: user_input)
  {


    for (auto i:labels)
    {
      for (auto b:zipped[i])
      {
      //cout << b[0]<< " "<< b[1]<< endl;
        final_dict[i] *= functional_density(i, b[0], b[1]);
      }
    }

  }




}
