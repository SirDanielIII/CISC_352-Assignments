(define (domain Dungeon)

    (:requirements
        :typing
        :negative-preconditions
        :conditional-effects
        :equality
     :disjunctive-preconditions)

    ; Do not modify the types
    (:types
        location colour key corridor
    )

    ; Do not modify the constants
    (:constants
        red yellow green purple rainbow - colour
    )

    ; You may introduce whatever predicates you would like to use
    (:predicates

        ; One predicate given for free!
        (hero-at ?loc - location)
        (messy ?loc - location)
        (holding ?key - key)
        (holding-any-key)
        (connected ?loc - location ?cor - corridor)
        (key-at ?key - key ?loc - location)
        (locked ?cor - corridor ?col - colour)
        (risky ?cor - corridor)
        (key-colour ?key - key ?col - colour)
        (one-use ?key - key)
        (two-uses ?key - key)
        (multi-use ?key - key)

    )

    ; IMPORTANT: You should not change/add/remove the action names or parameters

    ;Hero can move if the
    ;    - hero is at current location ?from,
    ;    - hero will move to location ?to,
    ;    - corridor ?cor exists between the ?from and ?to locations
    ;    - there isn't a locked door in corridor ?cor
    ;Effects move the hero, and collapse the corridor if it's "risky" (also causing a mess in the ?to location)
    (:action move

        :parameters (?from ?to - location ?cor - corridor)

        :precondition (and

            (hero-at ?from)  ; hero is at current location ?from
            (and (connected ?from ?cor)(connected ?to ?cor))  ; corridor ?cor exists between the ?from and ?to locations
            
            ; there isn't a locked door in the corridor ?cor with any colour lock
            (not (locked ?cor red))
            (not (locked ?cor green)) 
            (not (locked ?cor yellow)) 
            (not (locked ?cor purple)) 
            (not (locked ?cor rainbow)) 

        )

        :effect (and

            (not (hero-at ?from))  ; move the hero from the location ?from
            (hero-at ?to)  ; move the hero to the ?to location
            
            ; Collapse the corridor if it's "risky", causing a mess in the ?to location
            (when (risky ?cor)
                (and
                    (not (connected ?from ?cor))  ; collapse the corridor
                    (not (connected ?to ?cor))  ; collapse the corridor
                    (messy ?to)  ; cause a mess in the ?to location
                )
            )

        )
    )

    ;Hero can pick up a key if the
    ;    - hero is at current location ?loc,
    ;    - there is a key ?k at location ?loc,
    ;    - the hero's arm is free,
    ;    - the location is not messy
    ;Effect will have the hero holding the key and their arm no longer being free
    (:action pick-up

        :parameters (?loc - location ?k - key)

        :precondition (and

            (hero-at ?loc)  ; hero is at current location ?loc
            (key-at ?k ?loc)  ; there is a key ?k at location ?loc
            (not (holding-any-key))  ; the hero's arm is free
            (not (messy ?loc))  ; the location is not messy

        )

        :effect (and

            (holding ?k)  ; the hero is holding the key ?k
            (holding-any-key)  ; their arm is no longer free
            (not (key-at ?k ?loc))  ; key ?k is no longer at location ?loc

        )
    )

    ;Hero can drop a key if the
    ;    - hero is holding a key ?k,
    ;    - the hero is at location ?loc
    ;Effect will be that the hero is no longer holding the key
    (:action drop

        :parameters (?loc - location ?k - key)

        :precondition (and

            (holding ?k)  ; the hero is holding a key ?k
            (hero-at ?loc)  ; the hero is at location ?loc

        )

        :effect (and

            (not (holding ?k))  ; the hero is no longer holding the key ?k
            (not (holding-any-key))  ; hero is not holding any key now
            (key-at ?k ?loc)  ; key is now at current location

        )
    )


    ;Hero can use a key for a corridor if
    ;    - the hero is holding a key ?k,
    ;    - the key still has some uses left,
    ;    - the corridor ?cor is locked with colour ?col,
    ;    - the key ?k is if the right colour ?col,
    ;    - the hero is at location ?loc
    ;    - the corridor is connected to the location ?loc
    ;Effect will be that the corridor is unlocked and the key usage will be updated if necessary
    (:action unlock

        :parameters (?loc - location ?cor - corridor ?col - colour ?k - key)

        :precondition (and

            (holding ?k)  ; the hero is holding a key ?k
            (not (and (not (one-use ?k)) (not (two-uses ?k)) (not (multi-use ?k))))  ; the key still has some uses left
            (locked ?cor ?col)  ; the corridor ?cor is locked with colour ?col
            (key-colour ?k ?col)  ; the key ?k is in the right colour ?col
            (hero-at ?loc)  ; the hero is at location ?loc
            (connected ?loc ?cor)  ; the corridor ?cor is connected to the location ?loc

        )

        :effect (and

            (not (locked ?cor ?col))  ; the corridor ?cor is unlocked
            
            ; The key usage will be updated if necessary
            (when (two-uses ?k)
                (and
                    (not (two-uses ?k))  ; key ?k is no longer two-uses
                    (one-use ?k)  ; key ?k is now one-use
                )
            )
            (when (one-use ?k)
                (not (one-use ?k))  ; key ?k is no longer usable
            )

        )
    )

    ;Hero can clean a location if
    ;    - the hero is at location ?loc,
    ;    - the location is messy
    ;Effect will be that the location is no longer messy
    (:action clean

        :parameters (?loc - location)

        :precondition (and

            (hero-at ?loc)  ; the hero is at location ?loc
            (messy ?loc)  ; the location ?loc is messy

        )

        :effect (and

            (not (messy ?loc))  ; the location is no longer messy

        )
    )

)
