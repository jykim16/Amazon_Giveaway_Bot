TYPES OF GIVEAWAY:
1. Watch a short video
- Continue to entry (aria-labelledby="enter-youtube-video-button-announce")

2. No entry requirement
- Enter (class="a-button-input")
- Tap here to see if you win (class="a-section absoluteClickTargetContainer boxClickTarget giveaway-transparent")
3. Follow ...
4. Subscribe to a newsletter

TYPES OF WINNER MODELS
1. awarded randomly (1/N)
2. awarded at a set interval (Nth)
3. first N participants (first N)
- Jonathan, you didn't win (class="a-size-base-plus a-color-secondary qa-giveaway-result-text a-text-bold")

4. selected randomly after entry ended
- The winner will be notified via email after Aug 10, 2018 11:59 PM PDT. (class="a-size-small a-color-secondary qa-giveaway-winner-declare-time-text")

POSSIBLE ISSUES
- verify mobile phone number before entering
  - ask with password to enter in case messaged
  - send link to phone (human must enter code)

DATABASE DESIGN
1. schema
- ENTRIES (TABLE)
  - date-entered
  - date-results
  - entry-requirements (ENTRY-REQUIREMENTS)
  - results (RESULTS)
  - prize
  - prize-value
  - text-data
    - ?
- RESULTS (TABLE)
  - result
    - win
    - lose
    - deferred
  - count
- ENTRY-REQUIREMENTS (TABLE)
  - giveaway-type
  - query-selector (array/generator?)
  - count
