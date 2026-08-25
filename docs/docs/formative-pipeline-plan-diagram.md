[View live](https://mermaid.live/edit#pako:eNqFVl1z6jYQ_SsaP3TIDKQJ3JCEh04J5GbauclNITOZ1vAg7MVWkSVfWYbSkP_elWQbG0iah2BJ-3H2eM_Kb14gQ_AG3pLLTRBTpcnLeKZmguBfFPgPTJMBGckkYXpOOp1fds8KOoFd70jAW-6IcCb0WekXcGOJ7inNsrdn_Pe-D2n2bKA_IduRsX_HZbAiLuL8hNmT3JF7f7Q_r2zSAt1znsUFNpnpTorLnQWE4EJoQovSQ8Mo1ZDp1iQXxDxklanxc3WkJ-qwXrXj_UGzQEH9J0looJkU8xNGpryN_0qVICGsgcsUVKNMqVjEBOV46o8rC5s5Uf4jqAjIBH7kBo6WZDYTqWIJVVuyUFQEMWRV2kRZNwVrBpuW-6nKdUtrgKlaVapTBpS1vn17xLRm57RJpqlmgWW0NYFIQZYhAwcUY6IaIsvy44Q0iKbswKI8MJEqFkdSaMoEKMJhqYnKhWAiIkupSJwnVBT-oHYnIjXRN95MjfwPrOxLXuSMh1hxBP6deSRT81zxvj-2tdhlKIPMfwCETDWQn4jzG-Pup25LhZUWSb6aZ3Ivwk89gpIaf6TA5LqjwQpESPac_ZZ8glaDUhSJTOy-_1IuyURyTr5KtaEqbHRs08OyNIaUy-2O0E3mD1-nzVyGCtczPX_aQyYQn7bvbg3KdA2ERTsRZB30AUOWksK_cVBVbiE4zjZMx0YjRWQi8mRhugIC5d-PJtjSEcu02jYKyvJFpGgakxfTvdXuvsP9qYNnz-eFhlLUXrBCIaXINipxS7KAirMT7g48xSk0HU5fyDrnpi0WjDP9f06IGwlpTd0vZtVgR82HHsEP6sbiHzk18c_qhZagawpG4eYcgbkCkTlTI9KUSlUTsgF_5FQdFuA-OkdIJ8-aJbj9mmFdwkcmw1_fSBbTFAbEtFebcLoAPiAzz0EnVAUxW8PMI9WoGbrZxkHp_aQlQ7PO5seA7Lj6_jwkk5wDyhAbNoAEhB4YmmodYVmLEVwssQPtdKsGjHkxS8q4P4G_8c0dXhT7TPthU8orVNuaGsc48PEOOylEtKykjM8WeFofsrUDa-gSKYgMvA-N6vjraQs_vzb2LQ3TnOn9mCmsiukeHYMqNo-oOnVeEONuhMO5Xu77QxxYVqL2JVRIUJ51-AHOE380-f5EfpeLQs0bAL7atl4BVnxLrEbO6vZO8ghu2xqb_2TUMHHuTn8cqDDTZgwcxUrM0GFm_mYEuwP7Tcd4XV2Vo2-PshYj69ko_qNcg_Eqp-OScQyDHwEPnAas-I6wuraYrCtOE7Tm4E_xyQ5Zu8QbiEsRdThqIjz-cqjcSv2hKKyOzOTDXbeot21pUH5QWFllRldOVqmSSaot2sR-w_xMsq0I8Ce0xHwYywYq1NvIXkp67rW9SLHQG2iVQ9vD8Ak1S-_NRJx5OkaZzjwzDEKqVjNvJt7RJ6XiLymT0k3JPIq9wZLyDFd5GuLdOWYUL4K9CXYOqJHMhfYG17c2hDd48_7xBhfnt_1uv3fbvez2L256vesvbW_rDTq31-dX17hxc9u96Xa7_f572_vXZr087_UvLr5c3vT6_Zurfv_yqu1ByLRUj-4L3X6ov_8HqwkDCg)

```mermaidjs
flowchart TD
    gc[Git : Commit] -->|Pre-commit| cl(Commit lint)
    cl --> gcpass{Pass}
    gcpass -->|Yes| D[Block commit]
    gcpass -->|No| E[Commit]

    gp[Git : Push] -->|Post-push| lint(Code lint)
    gp -->|Post-push| gptest(Run tests)
    lint --> gppass{Pass}
    gptest --> gppass
    gppass -->|Yes| na[No action]
    gppass -->|No| w[Warn developer]

    originaldev[Developer] --> mr[Merge Request to \nprimary branches]
    mr --> review(review)
    review --> dev(Developer)
    review --> ai(LLM Reviewer)
    review --> statictests(Regression tests)
    dev --> reviewpass{MR Pass}
    ai --> reviewpass
    testpass -->|Container left running for human reviewer| reviewpass
    
    reviewpass -->|No| originaldev
    reviewpass -->|Yes| buildstage[Build Stage]
    buildstage --> builddocs[Generate & Build Docs]
    buildstage --> buildfront[Build Front End]
    buildstage --> buildcontainer[Create Backend Container Image]
    buildstage --> terraformbuild[Terraform Roll Forward]

    terraformbuild -->|Deploy| aws[AWS]
    builddocs --> s3[S3 Bucket for versioned static assets]
    buildfront --> s3
    buildcontainer -->|Build with \nversion number| ecr[ECR Registry]

    subgraph Tests
    statictests[Static Tests] --> depcheck(Dependancy scan)
    statictests --> sast(SAST vulnerability scan)
    statictests --> secrets(Secrets detection)
    statictests --> cqa(Code Quality)

    depcheck --> staticresult(Static \nTest Reports)
    sast --> staticresult
    secrets --> staticresult
    cqa --> staticresult

    staticresult --> staticpass
    staticresult --> A@{ shape: docs, label: "Report archive" }
    A --> alert[Developer Alerts]

    staticpass{OPA Rule Enforcement: \nStatic Test \nThreshold Pass} -->|No| testfail[Reject action]
    staticpass -->|Yes| terrafordry[Terraform Dry Run]

    terrafordry --> terrdrypass{pass}
    terrdrypass --> |Yes| regtest
    terrdrypass --> |No| testfail

    regtest[Regression Test Suite]
    regtest --> regpass{pass}
    regpass -->|No| testfail
    regpass -->|Yes| testpass
    
    testpass[All Tests Pass]
    end

    cron[CRON Jobs] --> weelky(Weekly check)
    cron --> daily(Daily Check)
    weelky --> cleanecr[Delete ECR images older than 5 versions]
    weelky --> s3clean[Move old static files to Glacier]
    daily --> scanstale[Scan for stale & long-lived branches]
    scanstale --> stalereport[Stale report]
    stalereport --> devalerts[Devloper prompts to merge / sync / delete]
    stalereport --> alertarchive[Stale report archive]
```

last updated 13-07-2026 1601
