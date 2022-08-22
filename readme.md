**Decay Script Documentation**
------------------------------

Decay script is a scripting language designed to easily create decay chain datapacks for the minecraft mod "Alive - Dynamic Ecosystems & Block Decay".

When the generated datapack is imported to a world in a minecraft instance running Alive 1.4+, these decay chains will overide the defaults.

The language itself is a verbose language and general syntax is as follows:

* chain {\<namespace>:\<block>[\<yValue>]>...}
    * used to define a decay chain.
    * an example of a decay chain:
        * ```
            chain {
                :stone_bricks[-1]>
                :mossy_stone_bricks[-1]>
                :cracked_stone_bricks[-1]>
                :cobblestone[-1]
            };
            ```
        * What this block of code is saying is kind of like this: If the block bellow the decay handler (as defined by [-1]) is stone bricks, convert it to the next in the list. (IE: mossy_stone_bricks). If it is mossy_stone_bricks, convert it to cracked, and so on and so forth from there.
* case \<namespace>:\<block>[\<yValue>],... {*more code...*}
    * a case clause allows you to insert an extra if block into any decay chains ran by the case clause. 
    * Within the case clause, any commands ran should end with a "/" instead of a ";" (so chain {}; would become chain {}/).
    * an example of a case clause with an imbeded chain:
        * ```
            case mca:loosegravel[-1] {
                chain {
                    mca:loosegravel[-2]>
                    :air[-2]
                }/
            };
            ```
        * What this block of code is saying is kind of similar to this: If the block bellow the decay handler is loosegravel (as defined by the [-1]), than run the following chain: if the block 2 blocks bellow is loosegravel, replace it with air. Another way of writing this in sudo code would be:
        ```
            decay chain {
                if (block -2 bellow == mca:loosegravel) {
                    replace with air
                } 
            }

            if (block -1 bellow == mca:loosegravel) {
                run (decay chain)
            }
        ```
    * Note: running a case clause inside of a case clause or sec clause may cause weird behaviour and possibly invalid datapacks.
* sec[\<name>] {*more code...*}
    * a sec clause essentially allows you to block different chains together, effectively giving them there own categories. 
    * Similar to a function, a sec may be reran with options by a run command (see bellow). 
    * An example of a sec clause is as follows:
        * ```
            sec[stone] {
                chain {
                    :stone_bricks[-1]>
                    :mossy_stone_bricks[-1]>
                    :cracked_stone_bricks[-1]>
                    :cobblestone[-1]
                }/
            };
            ```
        * This has the exact same functionality as the first decay chain code. However, the difference here is that if you call \<stone> using a run clause, you can rerun it if need be.
* run \<\<name>>[\<modifier>]
    * a run clause is used to rerun already defined secs.
    * The name argument specifies the predefined name of the sec being ran.
    * The modifier overides the yValue on all chain nodes within a decay chain.
        * so ```minecraft:stone_bricks[-1]>``` will become ```minecraft:stone_bricks[-2]>``` if the sec clause example is ran with this run command: ```run <stone>[-2]```.
    

A full example of the default decay chains written in decay script can be found in the file "```main.ds```".