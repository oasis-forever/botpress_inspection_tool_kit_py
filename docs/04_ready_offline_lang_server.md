## 4. Ready Offline Language Server

### 4-1. Download Required Files

Download embeddings(300 dimensions) and bpe files corresponding Japanese language.

* embeddings: http://botpress-public.nyc3.digitaloceanspaces.com/embeddings/bp.ja.300.bin
* bps: http://botpress-public.nyc3.digitaloceanspaces.com/embeddings/bp.ja.bpe.model

### 4-2. Place Downloaded Files

Place embeddings and bpe files as follows.

```
/botpress-v12_10_7-darwin-x64
 ├── lang
     ├── bp.ja.300.bin
     └── bp.ja.bpe.model
```

### 4-3. Change The Endpoint of Language Server

Change the parameter of `languageSources.endpoint` in `data/global/config/nlu.json` from `https://lang-01.botpress.io` to `http://localhost:3100` as follows.

* Before

```json
{
  "$schema": "../../assets/modules/nlu/config.schema.json",
  "ducklingURL": "https://duckling.botpress.io",
  "ducklingEnabled": true,
  "autoTrainInterval": "30s",
  "preloadModels": true,
  "languageSources": [
    {
      "endpoint": "https://lang-01.botpress.io"
    }
  ]
}
```

* After

```json
{
  "$schema": "../../assets/modules/nlu/config.schema.json",
  "ducklingURL": "https://duckling.botpress.io",
  "ducklingEnabled": true,
  "autoTrainInterval": "30s",
  "preloadModels": true,
  "languageSources": [
    {
      "endpoint": "http://localhost:3100"
    }
  ]
}
```

### 4-4. Boost Language Server

Boost the offline language server with `--offline`, `--dim` and `--langDir` arguments.

```bash
$ ./bp lang --offline --dim 300 --langDir lang
11/09/2020 13:02:05.056 Launcher ========================================
                                         Botpress Language Server        
                                                OS darwin               
                                 ========================================
11/09/2020 13:02:05.059 Launcher authToken: disabled (anyone can query your language server)
11/09/2020 13:02:05.059 Launcher adminToken: disabled (anyone can add, remove or change languages)
11/09/2020 13:02:05.059 Launcher limit: disabled (no protection - anyone can query without limitation)
11/09/2020 13:02:05.059 Launcher mode: offline (languages need to be downloaded manually from a machine with Internet access)
11/09/2020 13:02:05.060 Launcher Serving 300 language dimensions from lang
11/09/2020 13:02:05.062 Service Found Languages: ja
11/09/2020 13:02:05.062 Service Loading Embeddings for JA
11/09/2020 13:02:05.063 API Language Server is ready at http://localhost:3100/
11/09/2020 13:02:11.055 Service [JA] Took 5991ms to load 2851mb into RAM (lang/bp.ja.300.bin)
11/09/2020 13:02:11.161 Service [JA] Took 105ms to load 33mb into RAM (lang/bp.ja.bpe.model)
```

It is OK if you have seen that embeddings and bpe files are loaded on the log.

### 4-5. Language

Set the language to `Japanese` as you did in [2. Ready Botpress > 2-4. Language](https://github.com/oasis-forever/botpress_inspection_tool_kit_py/blob/master/docs/02_ready_botpress.md#2-4-language) with the offline server on.
