# py-es3

A small library for decrypting and encrypting to Unity's EasySave3 save file format.

It should be stated that this library only handles giving you the contents of a file, or putting content into a file. It does **not** transform that data into usable formats for you.

The reason for this is that EasySave3 [allows non-JSON like standards](https://docs.moodkie.com/easy-save-3/es3-guides/es3-supported-types/) and as such Python cannot translate it easily. Some examples of handling this later can be found in my other library for Phasmophobia saves - [Yurei](https://github.com/AbstractUmbra/Yurei).

Some examples of non-JSON data I've seen in these saves:-

#### Int keys

```json
{
    "playedMaps": {
        "__type": "System.Collections.Generic.Dictionary`2[[System.Int32, mscorlib, Version=4.0.0.0, Culture=neutral, PublicKeyToken=b77a5c561934e089],[System.Int32, mscorlib, Version=4.0.0.0, Culture=neutral, PublicKeyToken=b77a5c561934e089]],mscorlib",
        "value": {
            0: 159,
            12: 6,
            2: 4,
            3: 1,
            5: 3,
            8: 22,
            6: 2,
            42: 2
        }
    },
}
```

##### object keys

```json
{
        "LocalPlayerOutfit": {
        "__type": "PlayerOutfit,Assembly-CSharp",
        "value": {
            "Items": {
                {
                    "low": 16,
                    "high": 0
                }: {
                    "guid": {
                        "value": "722be916-7280-4ca7-b327-d8809ce035fd"
                    },
                    "materialOption": 0
                },
                {
                    "low": 8,
                    "high": 0
                }: {
                    "guid": {
                        "value": "722be916-7280-4ca7-b327-d8809ce035fd"
                    },
                    "materialOption": 0
                },
                {
                    "low": 1024,
                    "high": 0
                }: {
                    "guid": {
                        "value": "ef62365c-a1ad-4a12-9605-203e89b01ec3"
                    },
                    "materialOption": 0
                },
                {
                    "low": 256,
                    "high": 0
                }: {
                    "guid": {
                        "value": "ef62365c-a1ad-4a12-9605-203e89b01ec3"
                    },
                    "materialOption": 0
                },
                {
                    "low": 512,
                    "high": 0
                }: {
                    "guid": {
                        "value": "ef62365c-a1ad-4a12-9605-203e89b01ec3"
                    },
                    "materialOption": 0
                },
                {
                    "low": 128,
                    "high": 0
                }: {
                    "guid": {
                        "value": "3d8494a7-9d4c-489e-be97-8a6986c728d2"
                    },
                    "materialOption": 0
                },
                {
                    "low": 64,
                    "high": 0
                }: {
                    "guid": {
                        "value": "452dd4d1-5e6b-4775-923d-f896f97946c5"
                    },
                    "materialOption": 0
                },
                {
                    "low": 67108864,
                    "high": 0
                }: {
                    "guid": {
                        "value": "bf59eca4-4a14-47f5-8550-e73ab8955488"
                    },
                    "materialOption": 0
                },
                {
                    "low": 268435456,
                    "high": 0
                }: {
                    "guid": {
                        "value": "c8b6c096-7acd-46b5-8ca5-d1db4f3a8f07"
                    },
                    "materialOption": 0
                },
                {
                    "low": 134217728,
                    "high": 0
                }: {
                    "guid": {
                        "value": "4a1a766b-20a7-47c5-8fc5-dec3d1b23dd6"
                    },
                    "materialOption": 0
                },
                {
                    "low": 1,
                    "high": 0
                }: {
                    "guid": {
                        "value": "acaed4b3-29b2-4015-9c5a-ace1f9cf76e5"
                    },
                    "materialOption": 0
                },
                {
                    "low": 4,
                    "high": 0
                }: {
                    "guid": {
                        "value": "29e31646-23dc-447f-a7f5-1b258070ae77"
                    },
                    "materialOption": 4
                },
                {
                    "low": -2147483648,
                    "high": 0
                }: {
                    "guid": {
                        "value": "811a9257-ed4b-4e87-aa34-1faa53d11e43"
                    },
                    "materialOption": 0
                },
                {
                    "low": 0,
                    "high": 1
                }: {
                    "guid": {
                        "value": "1073b4c7-c896-4c66-853c-011f2c39bd55"
                    },
                    "materialOption": 0
                }
            }
        }
    },
}
```

So handling the data you get is on you!
