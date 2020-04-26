# genetic_algorithm_oe

Function optimizing with genetic algoritm, can optimize any function in any dimension, 
can search for minimum and maximum in given range.

## Sample functions:
  * Levy function
  * Michalewicz function
  * Bukin function
  * Damavandi function

## Parameters to configure:
  * Optimizing function
  * Searching value _min_ or _max_
  * Chromosome representation _RealChromosome_ or _BinaryChromosome_
  * Number of chromosomes in individual, corresponds with number of dimensions in function
  * Accuracy for _BinaryChromosome_
  * Range in which function optimum will be searching for. _range_start_ and _range_end_
  * Number of epochs
  * Size of population
  * Selection type with proper parameter: 
    + Roulette with number to select parameter, 
    + By best value with number to select parameter,
    + Tournament selection with tournament size parameter 
  * Chromosome crossover type depending on chromosome representation
    + Binary Chromosome
      + one point crossing
      + two points crossing
      + three points crossing
    + Real Chromosome
      + arithmetic crossing
      + heuristic crossing
  * Chromosome mutation
      + Binary Chromosome
        + one point mutation
        + two points mutation
        + three points mutation
        + border mutation
      + Real Chromosome
        + even mutatation
        + mutation by index change
  * Inversion operator only for Binary chromosome
  * Elite strategy with number parameter, keeping number of best individuals in whole evolution process.

## Run

Run with main.py as console application or MainPage.py to run as window application.

## Implementation

Chromosome representation and most calculations are implemented with numpy arrays.
