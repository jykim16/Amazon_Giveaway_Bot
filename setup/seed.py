from db import session, Result, Entry_Requirement, Entry

# add possible results
session.add_all([
    Result(result='win'),
    Result(result='lose'),
    Result(result='deferred')
])

# add possible entry conditions
session.add_all([
    Entry_Requirement(giveaway_type='Watch a short video',
                        query_selector="('.continue_button_inner', '.boxClickTarget')"),
    Entry_Requirement(giveaway_type='No entry requirement',
                        query_selector="('.boxClickTarget', '.a-button-input')"),
    Entry_Requirement(giveaway_type='Follow * on *',
                        query_selector="('.a-button-input','.a-button-input', '.boxClickTarget')"),
    Entry_Requirement(giveaway_type='Subscribe to a newsletter',
                        query_selector="('.a-button-input')"),
])

session.commit()

#result: a-size-base-plus a-color-secondary qa-giveaway-result-text a-text-bold
#deferred result: a-size-base-plus a-color-secondary qa-giveaway-result-text a-text-bold
    #time: a-size-small a-color-secondary qa-giveaway-winner-declare-time-text
    #Aug 17, 2018 11:59 PM PDT

# prize_image in #prize-image
# prize in .qa-prize-name-label
