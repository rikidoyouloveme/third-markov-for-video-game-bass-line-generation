# Third degree Markov model for generating bass lines for video game soundtracks

### Dataset

Source: [hansespinosa2 - 30000 Video Game MIDI Files](www.kaggle.com/datasets/hansespinosa2/40000-video-game-midi-files/data)

### Project structure

* Analysis, model creation and file generation - [project.ipynb](project.ipynb)
* Package requirements - [requirements.txt](requirements.txt)
* Dataset download - [download_data.py](download_data.py)

### Theoretical basis

A Markov model is a

### Training dataset

### Dataset preprocessing

The MIDI files were mostly composed of more than one track and instrument.

![histogram_num_of_tracks](image/README/histogram_num_of_tracks.png)

An analysis of the most common instrument to do the training and generation for was done by splitting all instrument names in all MIDI files and analyzing the unique word histogram. Only the words which were present more  than 20 times are shown:

![histogram_common_words](image/README/histogram_common_words.png)

Since bass was the most common instrument name on the histogram, it was decided to create a Markov model to generate bass guitar lines from the dataset.
The bass intruments were still needed to be filtered to remove intruments like the bassoon, bass saxophone, bass echo, and so on. For this another histogram was generated:
![histogram_bass_instruments](image/README/histogram_bass_instruments.png)
An important part was also to make sure the files didn't have some outliers. One way of making sure was looking at the hsitogram of MIDI file durations:

![histogram_duration](image/README/histogram_duration.png)

From here it was decided to remove the files with duration longer than 200 seconds.

* After preprocessing there are 2459 valid MIDI files for model training.

### Model creation

Events which were created:

* pitch
* duration
* onset gap
* chord

Number of states: 1908
Number of tokens: 1040935

Number of contexts per order: 1 - 1905; 2 - 19749; 3 - 56846.

#### Data sparsity and rare-state collapsing

Unique raw (pitch, duration, gap, chord) tokens: 2568
Share of unique tokens that occur < 2 times (collapsed to UNK): 25.7%
Share of all training tokens that end up as UNK: 0.1%
Share of contexts seen exactly once, per order: {1: '0.4%', 2: '17.8%', 3: '19.7%'}

Two bass lines with MIDI files were generated for each temperature in the list: [0.5, 0.7, 0.9, 1, 1.15, 1.5]

### Model evaluation

<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: left;">
      <th>Group</th>
      <th>Pitch entropy</th>
      <th>Interval entropy</th>
      <th>Duration entropy</th>
      <th>3-gram Jaccard</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>original</td>
      <td>5.050</td>
      <td>3.481</td>
      <td>0.457</td>
      <td>1.000</td>
    </tr>
    <tr>
      <td>generated</td>
      <td>4.466</td>
      <td>3.132</td>
      <td>1.106</td>
      <td>0.025</td>
    </tr>
  </tbody>
</table>
</div>

#### Pitch, interval and duration comparison

![histogram_comparison](image/README/histogram_comparison.png)

#### Note transitions

![note_transitions](image/README/note_transitions.png)

#### Duration comparison

![duration_comparison](image/README/duration_comparison.png)

#### Held-out perplexity

Train songs: 1934 | Held-out test songs: 483
Held-out perplexity, order-3 model with backoff: 9.9
Held-out perplexity, unigram-only baseline: 66.2

#### Novelty check

<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: left;">
      <th>Temperature</th>
      <th>5-gram overlap with training</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>0.50</td>
      <td>1.000</td>
    </tr>
    <tr>
      <td>0.70</td>
      <td>0.957</td>
    </tr>
    <tr>
      <td>0.90</td>
      <td>0.891</td>
    </tr>
    <tr>
      <td>1.00</td>
      <td>0.935</td>
    </tr>
    <tr>
      <td>1.15</td>
      <td>0.750</td>
    </tr>
    <tr>
      <td>1.50</td>
      <td>0.859</td>
    </tr>
  </tbody>
</table>
</div>

#### Visual comparison

![visual_comparison](image/README/visual_comparison.png)

<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }
