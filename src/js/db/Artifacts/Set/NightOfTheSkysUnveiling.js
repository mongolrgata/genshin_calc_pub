import { ArtifactSet } from "../../../classes/ArtifactSet";
import { ConditionStatic } from "../../../classes/Condition/Static";
import { ConditionNot } from "../../../classes/Condition/Not";

export const NightOfTheSkysUnveiling = new ArtifactSet({
    serializeId: 56,
    goodId: 'NightOfTheSkysUnveiling',
    gameId: 15041,
    itemIds: [41412, 41413, 41422, 41423, 41432, 41433, 41442, 41443, 41452, 41453, 41513, 41514, 41523, 41524, 41533, 41534, 41543, 41544, 41553, 41554, 23781, 23782, 23783, 23784, 23785, 23786, 23787, 23788, 23789, 23790],
    name: "artifact_set.night_of_the_skys_unveiling",
    iconClass: "artifact-icon-night-of-the-skys-unveiling",
    minRarity: 4,
    maxRarity: 5,
    setBonus: [
        {},
        {
            conditions: [
                new ConditionStatic({
                    title: 'set_bonus.night_of_the_skys_unveiling_2',
                    description: 'set_descr.night_of_the_skys_unveiling_2',
                    stats: {
                        mastery: 80,
                    },
                })
            ],
        },
        {},
        {
            conditions: [
                new ConditionStatic({
                    name: 'set.night_of_the_skys_unveiling_4_1',
                    title: 'set_bonus.night_of_the_skys_unveiling_4',
                    description: 'set_descr.night_of_the_skys_unveiling_4_1',
                    condition: new ConditionNot([]),
                }),
                new ConditionStatic({
                    name: 'set.night_of_the_skys_unveiling_4_2',
                    title: 'set_bonus.night_of_the_skys_unveiling_4',
                    description: 'set_descr.night_of_the_skys_unveiling_4_2',
                    condition: new ConditionNot([]),
                }),
            ],
        },
    ],
});
