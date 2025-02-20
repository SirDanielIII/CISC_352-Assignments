(define (problem p4-dungeon)
  (:domain Dungeon)

  ; Come up with your own problem instance (see assignment for details)
  ; NOTE: You _may_ use new objects for this problem only.

  ; Naming convention:
  ; - loc-{i}-{j} refers to the location at the i'th column and j'th row (starting in top left corner)
  ; - c{i}{j}{h}{k} refers to the corridor connecting loc-{i}-{j} and loc-{h}-{k}
  (:objects
    loc-1-2 loc-2-1 loc-2-2 loc-3-2 loc-2-3 loc-3-3 loc-4-3 loc-3-4 - location
    c2212 c2221 c2223 c2232 c2233 c1223 c3233 c3334 c3343 - corridor
    key1 key2 key3 key4 key5 - key
  )

  (:init

    ; Hero location and carrying status
    (hero-at loc-2-2)

    ; Locationg <> Corridor Connections
    (connected loc-2-2 c2212) 
    (connected loc-1-2 c2212) 
    (connected loc-2-2 c2221) 
    (connected loc-2-1 c2221) 
    (connected loc-2-2 c2223) 
    (connected loc-2-3 c2223) 
    (connected loc-2-2 c2232) 
    (connected loc-3-2 c2232) 
    (connected loc-2-2 c2233)
    (connected loc-3-3 c2233)
    (connected loc-1-2 c1223) 
    (connected loc-2-3 c1223) 
    (connected loc-3-2 c3233) 
    (connected loc-3-3 c3233) 
    (connected loc-3-3 c3334) 
    (connected loc-3-4 c3334) 
    (connected loc-3-3 c3343)
    (connected loc-4-3 c3343)

    ; Key locations
    (key-at key1 loc-2-2)
    (key-at key2 loc-1-2)
    (key-at key3 loc-3-2)
    (key-at key4 loc-4-3)
    (key-at key5 loc-3-4)

    ; Locked corridors
    (locked c2212 red)
    (locked c2221 rainbow)
    (locked c2223 red)
    (locked c2232 red) 
    (locked c2233 red)
    (locked c1223 yellow)
    (locked c3233 yellow)
    (locked c3334 green)
    (locked c3343 purple)

    ; Risky corridors
    (risky c2212)
    (risky c2223)
    (risky c2232)
    (risky c2233)

    ; Key colours
    (key-colour key1 red)
    (key-colour key2 yellow)
    (key-colour key3 purple)
    (key-colour key4 green)
    (key-colour key5 rainbow)

    ; Key usage properties (one use, two use, etc)
    (multi-use key1)
    (two-uses key2)
    (one-use key3)
    (one-use key4)
    (one-use key5)

  )
  (:goal
    (and
      (hero-at loc-2-1)
      ; Hero's final location goes here
    )
  )

)
