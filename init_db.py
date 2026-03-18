{
  "scenario_a": {
    "baseline": {
      "avg_generation_time": 0.0001802206039428711,
      "avg_conflict_rate": 30.0,
      "avg_deadline_compliance_rate": 98.0,
      "avg_workload_std": 1.2502945727299848,
      "std_generation_time": 8.804929001890796e-05,
      "std_conflict_rate": 10.540925533894598
    },
    "agent": {
      "avg_generation_time": 0.0005606651306152344,
      "avg_conflict_rate": 28.0,
      "avg_deadline_compliance_rate": 98.0,
      "avg_workload_std": 1.1284958490373687,
      "std_generation_time": 0.00022185478167927335,
      "std_conflict_rate": 6.324555320336759
    },
    "raw_baseline": [
      {
        "schedule_generation_time": 0.0001475811004638672,
        "conflict_count": 3,
        "conflict_rate": 30.0,
        "deadline_compliance_count": 10,
        "deadline_compliance_rate": 100.0,
        "workload_distribution_std": 1.0205335853082955,
        "daily_hours": {
          "2026-03-09": 6.5493067911396325,
          "2026-03-08": 6.197342697660129,
          "2026-03-10": 4.632187945092464
        },
        "conflicts": [
          "Task 'Task A3' overlaps with locked block",
          "Task 'Task A4' overlaps with locked block",
          "Task 'Task A6' overlaps with locked block"
        ]
      },
      {
        "schedule_generation_time": 0.00030350685119628906,
        "conflict_count": 4,
        "conflict_rate": 40.0,
        "deadline_compliance_count": 10,
        "deadline_compliance_rate": 100.0,
        "workload_distribution_std": 2.691568202418998,
        "daily_hours": {
          "2026-03-10": 6.9240087370372185,
          "2026-03-09": 6.171962474906088,
          "2026-03-11": 1.0193119480587698,
          "2026-03-08": 5.90139039100363
        },
        "conflicts": [
          "Task 'Task A1' overlaps with locked block",
          "Task 'Task A6' overlaps with locked block",
          "Task 'Task A7' overlaps with locked block",
          "Task 'Task A8' overlaps with locked block"
        ]
      },
      {
        "schedule_generation_time": 0.00011467933654785156,
        "conflict_count": 1,
        "conflict_rate": 10.0,
        "deadline_compliance_count": 10,
        "deadline_compliance_rate": 100.0,
        "workload_distribution_std": 1.6134058270325644,
        "daily_hours": {
          "2026-03-10": 3.430829935729892,
          "2026-03-09": 6.044894990583904,
          "2026-03-08": 6.658078563293237,
          "2026-03-13": 3.2799229913663206,
          "2026-03-11": 3.0907091728758194,
          "2026-03-12": 3.2264089022400912
        },
        "conflicts": [
          "Task 'Task A6' overlaps with locked block"
        ]
      },
      {
        "schedule_generation_time": 0.0001049041748046875,
        "conflict_count": 3,
        "conflict_rate": 30.0,
        "deadline_compliance_count": 10,
        "deadline_compliance_rate": 100.0,
        "workload_distribution_std": 0.5042130222425825,
        "daily_hours": {
          "2026-03-10": 6.529922203879338,
          "2026-03-08": 5.306282154842572,
          "2026-03-11": 5.908472500221057,
          "2026-03-09": 5.77834920342631
        },
        "conflicts": [
          "Task 'Task A2' overlaps with locked block",
          "Task 'Task A4' overlaps with locked block",
          "Task 'Task A10' overlaps with locked block"
        ]
      },
      {
        "schedule_generation_time": 0.00010609626770019531,
        "conflict_count": 3,
        "conflict_rate": 30.0,
        "deadline_compliance_count": 10,
        "deadline_compliance_rate": 100.0,
        "workload_distribution_std": 0.9821334613895749,
        "daily_hours": {
          "2026-03-08": 6.3756358398994255,
          "2026-03-10": 4.142987226995074,
          "2026-03-09": 5.435705510594478,
          "2026-03-11": 6.030528195004959
        },
        "conflicts": [
          "Task 'Task A1' overlaps with locked block",
          "Task 'Task A2' overlaps with locked block",
          "Task 'Task A10' overlaps with locked block"
        ]
      },
      {
        "schedule_generation_time": 0.00011515617370605469,
        "conflict_count": 5,
        "conflict_rate": 50.0,
        "deadline_compliance_count": 8,
        "deadline_compliance_rate": 80.0,
        "workload_distribution_std": 0.811109330938606,
        "daily_hours": {
          "2026-03-08": 5.83775882211909,
          "2026-03-10": 5.381107549356136,
          "2026-03-12": 3.895108418759576,
          "2026-03-11": 4.8322297659366455,
          "2026-03-09": 5.805316832357064
        },
        "conflicts": [
          "Task 'Task A1' overlaps with locked block",
          "Task 'Task A2' scheduled past deadline (2026-03-09)",
          "Task 'Task A3' overlaps with locked block",
          "Task 'Task A8' overlaps with locked block",
          "Task 'Task A10' scheduled past deadline (2026-03-10)"
        ]
      },
      {
        "schedule_generation_time": 0.00012230873107910156,
        "conflict_count": 2,
        "conflict_rate": 20.0,
        "deadline_compliance_count": 10,
        "deadline_compliance_rate": 100.0,
        "workload_distribution_std": 1.1026454179022607,
        "daily_hours": {
          "2026-03-08": 4.734387248819864,
          "2026-03-14": 3.362002214111107,
          "2026-03-12": 3.709037558210436,
          "2026-03-11": 3.3866119012326696,
          "2026-03-13": 3.0535172595007656,
          "2026-03-10": 5.918636508054892,
          "2026-03-09": 5.2660693564083445
        },
        "conflicts": [
          "Task 'Task A6' overlaps with locked block",
          "Task 'Task A8' overlaps with locked block"
        ]
      },
      {
        "schedule_generation_time": 0.00018072128295898438,
        "conflict_count": 3,
        "conflict_rate": 30.0,
        "deadline_compliance_count": 10,
        "deadline_compliance_rate": 100.0,
        "workload_distribution_std": 1.9554407675410224,
        "daily_hours": {
          "2026-03-11": 2.7410925399182395,
          "2026-03-08": 6.175357050758525,
          "2026-03-10": 6.8576618470389725,
          "2026-03-09": 6.7794227617874645
        },
        "conflicts": [
          "Task 'Task A2' overlaps with locked block",
          "Task 'Task A4' overlaps with locked block",
          "Task 'Task A6' overlaps with locked block"
        ]
      },
      {
        "schedule_generation_time": 0.0003044605255126953,
        "conflict_count": 3,
        "conflict_rate": 30.0,
        "deadline_compliance_count": 10,
        "deadline_compliance_rate": 100.0,
        "workload_distribution_std": 0.5988191850137569,
        "daily_hours": {
          "2026-03-10": 5.01687627940084,
          "2026-03-08": 5.973199453043861,
          "2026-03-12": 5.832514881178245,
          "2026-03-11": 5.249142301613037,
          "2026-03-09": 6.520930041698157
        },
        "conflicts": [
          "Task 'Task A1' overlaps with locked block",
          "Task 'Task A2' overlaps with locked block",
          "Task 'Task A3' overlaps with locked block"
        ]
      },
      {
        "schedule_generation_time": 0.0003027915954589844,
        "conflict_count": 3,
        "conflict_rate": 30.0,
        "deadline_compliance_count": 10,
        "deadline_compliance_rate": 100.0,
        "workload_distribution_std": 1.2230769275121858,
        "daily_hours": {
          "2026-03-10": 6.572287059949763,
          "2026-03-09": 6.007043060776503,
          "2026-03-11": 6.465256273605849,
          "2026-03-12": 3.5693385728831,
          "2026-03-08": 5.531881362674956
        },
        "conflicts": [
          "Task 'Task A5' overlaps with locked block",
          "Task 'Task A9' overlaps with locked block",
          "Task 'Task A10' overlaps with locked block"
        ]
      }
    ],
    "raw_agent": [
      {
        "schedule_generation_time": 0.0006282329559326172,
        "conflict_count": 3,
        "conflict_rate": 30.0,
        "deadline_compliance_count": 10,
        "deadline_compliance_rate": 100.0,
        "workload_distribution_std": 1.0205335853082955,
        "daily_hours": {
          "2026-03-09": 6.5493067911396325,
          "2026-03-08": 6.197342697660129,
          "2026-03-10": 4.632187945092464
        },
        "conflicts": [
          "Task 'Task A3' overlaps with locked block",
          "Task 'Task A4' overlaps with locked block",
          "Task 'Task A6' overlaps with locked block"
        ]
      },
      {
        "schedule_generation_time": 0.0004913806915283203,
        "conflict_count": 3,
        "conflict_rate": 30.0,
        "deadline_compliance_count": 10,
        "deadline_compliance_rate": 100.0,
        "workload_distribution_std": 2.7645979312949955,
        "daily_hours": {
          "2026-03-10": 6.9240087370372185,
          "2026-03-09": 6.821530440600947,
          "2026-03-08": 5.25182242530877,
          "2026-03-11": 1.0193119480587698
        },
        "conflicts": [
          "Task 'Task A1' overlaps with locked block",
          "Task 'Task A3' overlaps with locked block",
          "Task 'Task A7' overlaps with locked block"
        ]
      },
      {
        "schedule_generation_time": 0.0003933906555175781,
        "conflict_count": 2,
        "conflict_rate": 20.0,
        "deadline_compliance_count": 10,
        "deadline_compliance_rate": 100.0,
        "workload_distribution_std": 1.2631530356530363,
        "daily_hours": {
          "2026-03-09": 5.7029726344356835,
          "2026-03-11": 5.283528413532921,
          "2026-03-08": 6.658078563293237,
          "2026-03-10": 4.859856042587331,
          "2026-03-12": 3.2264089022400912
        },
        "conflicts": [
          "Task 'Task A6' overlaps with locked block",
          "Task 'Task A10' overlaps with locked block"
        ]
      },
      {
        "schedule_generation_time": 0.0003368854522705078,
        "conflict_count": 3,
        "conflict_rate": 30.0,
        "deadline_compliance_count": 10,
        "deadline_compliance_rate": 100.0,
        "workload_distribution_std": 0.5042130222425825,
        "daily_hours": {
          "2026-03-10": 6.529922203879338,
          "2026-03-08": 5.306282154842572,
          "2026-03-11": 5.908472500221057,
          "2026-03-09": 5.77834920342631
        },
        "conflicts": [
          "Task 'Task A2' overlaps with locked block",
          "Task 'Task A4' overlaps with locked block",
          "Task 'Task A10' overlaps with locked block"
        ]
      },
      {
        "schedule_generation_time": 0.00035691261291503906,
        "conflict_count": 3,
        "conflict_rate": 30.0,
        "deadline_compliance_count": 10,
        "deadline_compliance_rate": 100.0,
        "workload_distribution_std": 0.8312036766847946,
        "daily_hours": {
          "2026-03-08": 6.3756358398994255,
          "2026-03-11": 4.39381265494665,
          "2026-03-09": 5.435705510594478,
          "2026-03-10": 5.779702767053383
        },
        "conflicts": [
          "Task 'Task A1' overlaps with locked block",
          "Task 'Task A6' overlaps with locked block",
          "Task 'Task A10' overlaps with locked block"
        ]
      },
      {
        "schedule_generation_time": 0.0004661083221435547,
        "conflict_count": 4,
        "conflict_rate": 40.0,
        "deadline_compliance_count": 8,
        "deadline_compliance_rate": 80.0,
        "workload_distribution_std": 0.8596219186964262,
        "daily_hours": {
          "2026-03-09": 5.604902170782534,
          "2026-03-10": 5.237021202193557,
          "2026-03-12": 3.895108418759576,
          "2026-03-08": 6.182259830856198,
          "2026-03-11": 4.8322297659366455
        },
        "conflicts": [
          "Task 'Task A3' overlaps with locked block",
          "Task 'Task A7' overlaps with locked block",
          "Task 'Task A9' scheduled past deadline (2026-03-09)",
          "Task 'Task A10' scheduled past deadline (2026-03-10)"
        ]
      },
      {
        "schedule_generation_time": 0.00037550926208496094,
        "conflict_count": 2,
        "conflict_rate": 20.0,
        "deadline_compliance_count": 10,
        "deadline_compliance_rate": 100.0,
        "workload_distribution_std": 1.0953210764445909,
        "daily_hours": {
          "2026-03-08": 4.734387248819864,
          "2026-03-13": 3.362002214111107,
          "2026-03-12": 3.709037558210436,
          "2026-03-11": 3.3866119012326696,
          "2026-03-14": 3.0535172595007656,
          "2026-03-10": 5.833527144162911,
          "2026-03-09": 5.351178720300325
        },
        "conflicts": [
          "Task 'Task A6' overlaps with locked block",
          "Task 'Task A8' overlaps with locked block"
        ]
      },
      {
        "schedule_generation_time": 0.0007536411285400391,
        "conflict_count": 2,
        "conflict_rate": 20.0,
        "deadline_compliance_count": 10,
        "deadline_compliance_rate": 100.0,
        "workload_distribution_std": 0.9916771948250299,
        "daily_hours": {
          "2026-03-11": 4.38424162385304,
          "2026-03-08": 5.360869176075017,
          "2026-03-10": 6.151823836034749,
          "2026-03-09": 6.656599563540395
        },
        "conflicts": [
          "Task 'Task A2' overlaps with locked block",
          "Task 'Task A3' overlaps with locked block"
        ]
      },
      {
        "schedule_generation_time": 0.0008935928344726562,
        "conflict_count": 3,
        "conflict_rate": 30.0,
        "deadline_compliance_count": 10,
        "deadline_compliance_rate": 100.0,
        "workload_distribution_std": 0.7232211078794946,
        "daily_hours": {
          "2026-03-10": 5.718172161297948,
          "2026-03-08": 5.973199453043861,
          "2026-03-12": 5.832514881178245,
          "2026-03-11": 4.5478464197159285,
          "2026-03-09": 6.520930041698157
        },
        "conflicts": [
          "Task 'Task A1' overlaps with locked block",
          "Task 'Task A2' overlaps with locked block",
          "Task 'Task A3' overlaps with locked block"
        ]
      },
      {
        "schedule_generation_time": 0.0009109973907470703,
        "conflict_count": 3,
        "conflict_rate": 30.0,
        "deadline_compliance_count": 10,
        "deadline_compliance_rate": 100.0,
        "workload_distribution_std": 1.2314159413444414,
        "daily_hours": {
          "2026-03-11": 6.309487177922362,
          "2026-03-09": 6.007043060776503,
          "2026-03-12": 3.5693385728831,
          "2026-03-08": 5.531881362674956,
          "2026-03-10": 6.728056155633251
        },
        "conflicts": [
          "Task 'Task A5' overlaps with locked block",
          "Task 'Task A9' overlaps with locked block",
          "Task 'Task A10' overlaps with locked block"
        ]
      }
    ]
  },
  "scenario_b": {
    "baseline": {
      "avg_generation_time": 0.00014607906341552735,
      "avg_conflict_rate": 51.25,
      "avg_deadline_compliance_rate": 63.75,
      "avg_workload_std": 1.0866558574372842,
      "std_generation_time": 7.543034088833678e-05,
      "std_conflict_rate": 13.756311682682648
    },
    "agent": {
      "avg_generation_time": 0.00042555332183837893,
      "avg_conflict_rate": 51.25,
      "avg_deadline_compliance_rate": 63.75,
      "avg_workload_std": 1.2653372051703058,
      "std_generation_time": 0.00018969575471464625,
      "std_conflict_rate": 13.756311682682648
    },
    "raw_baseline": [
      {
        "schedule_generation_time": 0.00031447410583496094,
        "conflict_count": 4,
        "conflict_rate": 50.0,
        "deadline_compliance_count": 4,
        "deadline_compliance_rate": 50.0,
        "workload_distribution_std": 0.2598413266372834,
        "daily_hours": {
          "2026-03-09": 3.8263235201693924,
          "2026-03-10": 3.421645500833725,
          "2026-03-11": 3.2591126741348675,
          "2026-03-13": 3.628188025854103,
          "2026-03-12": 3.9629815769968237,
          "2026-03-08": 3.523330688231006
        },
        "conflicts": [
          "Task 'Task B4' scheduled past deadline (2026-03-11)",
          "Task 'Task B5' scheduled past deadline (2026-03-11)",
          "Task 'Task B7' (ID:7) could not be scheduled",
          "Task 'Task B8' (ID:8) could not be scheduled"
        ]
      },
      {
        "schedule_generation_time": 0.0002512931823730469,
        "conflict_count": 5,
        "conflict_rate": 62.5,
        "deadline_compliance_count": 5,
        "deadline_compliance_rate": 62.5,
        "workload_distribution_std": 1.8789389077573233,
        "daily_hours": {
          "2026-03-09": 4.413797400094129,
          "2026-03-08": 5.9009942084846365,
          "2026-03-10": 2.168680612591173
        },
        "conflicts": [
          "Task 'Task B3' (ID:3) could not be scheduled",
          "Task 'Task B4' (ID:4) could not be scheduled",
          "Task 'Task B5' overlaps with locked block",
          "Task 'Task B6' (ID:6) could not be scheduled",
          "Task 'Task B7' overlaps with locked block"
        ]
      },
      {
        "schedule_generation_time": 9.679794311523438e-05,
        "conflict_count": 3,
        "conflict_rate": 37.5,
        "deadline_compliance_count": 7,
        "deadline_compliance_rate": 87.5,
        "workload_distribution_std": 0.8324038834058065,
        "daily_hours": {
          "2026-03-08": 5.018802196215885,
          "2026-03-09": 5.099889682478671,
          "2026-03-10": 5.454883130224192,
          "2026-03-11": 3.57003927888576
        },
        "conflicts": [
          "Task 'Task B1' overlaps with locked block",
          "Task 'Task B2' (ID:2) could not be scheduled",
          "Task 'Task B8' overlaps with locked block"
        ]
      },
      {
        "schedule_generation_time": 9.894371032714844e-05,
        "conflict_count": 5,
        "conflict_rate": 62.5,
        "deadline_compliance_count": 5,
        "deadline_compliance_rate": 62.5,
        "workload_distribution_std": 2.115665027039061,
        "daily_hours": {
          "2026-03-10": 2.409245937352204,
          "2026-03-08": 6.282634579014653,
          "2026-03-09": 5.82098630590154
        },
        "conflicts": [
          "Task 'Task B1' (ID:1) could not be scheduled",
          "Task 'Task B2' overlaps with locked block",
          "Task 'Task B3' (ID:3) could not be scheduled",
          "Task 'Task B4' overlaps with locked block",
          "Task 'Task B8' (ID:8) could not be scheduled"
        ]
      },
      {
        "schedule_generation_time": 0.0001246929168701172,
        "conflict_count": 5,
        "conflict_rate": 62.5,
        "deadline_compliance_count": 3,
        "deadline_compliance_rate": 37.5,
        "workload_distribution_std": 0.3186420193014229,
        "daily_hours": {
          "2026-03-10": 3.56268570575868,
          "2026-03-09": 3.1246776373188636,
          "2026-03-08": 3.7445680748747803
        },
        "conflicts": [
          "Task 'Task B1' (ID:1) could not be scheduled",
          "Task 'Task B3' (ID:3) could not be scheduled",
          "Task 'Task B4' (ID:4) could not be scheduled",
          "Task 'Task B5' (ID:5) could not be scheduled",
          "Task 'Task B8' (ID:8) could not be scheduled"
        ]
      },
      {
        "schedule_generation_time": 0.00010418891906738281,
        "conflict_count": 4,
        "conflict_rate": 50.0,
        "deadline_compliance_count": 5,
        "deadline_compliance_rate": 62.5,
        "workload_distribution_std": 1.4428306913499562,
        "daily_hours": {
          "2026-03-09": 5.782683110370829,
          "2026-03-08": 6.21979278594576,
          "2026-03-10": 3.5310188161088196
        },
        "conflicts": [
          "Task 'Task B2' overlaps with locked block",
          "Task 'Task B3' (ID:3) could not be scheduled",
          "Task 'Task B4' (ID:4) could not be scheduled",
          "Task 'Task B6' (ID:6) could not be scheduled"
        ]
      },
      {
        "schedule_generation_time": 9.846687316894531e-05,
        "conflict_count": 3,
        "conflict_rate": 37.5,
        "deadline_compliance_count": 6,
        "deadline_compliance_rate": 75.0,
        "workload_distribution_std": 1.2219861374491279,
        "daily_hours": {
          "2026-03-11": 3.269543729124809,
          "2026-03-09": 5.712256629445042,
          "2026-03-08": 5.5356625287807795,
          "2026-03-10": 3.8268028247296897
        },
        "conflicts": [
          "Task 'Task B3' (ID:3) could not be scheduled",
          "Task 'Task B4' (ID:4) could not be scheduled",
          "Task 'Task B7' overlaps with locked block"
        ]
      },
      {
        "schedule_generation_time": 0.00012254714965820312,
        "conflict_count": 5,
        "conflict_rate": 62.5,
        "deadline_compliance_count": 3,
        "deadline_compliance_rate": 37.5,
        "workload_distribution_std": 0.36589809243684496,
        "daily_hours": {
          "2026-03-10": 3.856064897504122,
          "2026-03-08": 3.847837295600545,
          "2026-03-09": 3.176441316367831,
          "2026-03-11": 3.9871539768145827
        },
        "conflicts": [
          "Task 'Task B2' (ID:2) could not be scheduled",
          "Task 'Task B5' scheduled past deadline (2026-03-10)",
          "Task 'Task B6' (ID:6) could not be scheduled",
          "Task 'Task B7' (ID:7) could not be scheduled",
          "Task 'Task B8' (ID:8) could not be scheduled"
        ]
      },
      {
        "schedule_generation_time": 0.00010037422180175781,
        "conflict_count": 5,
        "conflict_rate": 62.5,
        "deadline_compliance_count": 5,
        "deadline_compliance_rate": 62.5,
        "workload_distribution_std": 2.0129625789220005,
        "daily_hours": {
          "2026-03-08": 6.403115141581219,
          "2026-03-09": 5.80499886827144,
          "2026-03-10": 2.6561956786658825
        },
        "conflicts": [
          "Task 'Task B2' (ID:2) could not be scheduled",
          "Task 'Task B3' (ID:3) could not be scheduled",
          "Task 'Task B5' overlaps with locked block",
          "Task 'Task B6' overlaps with locked block",
          "Task 'Task B8' (ID:8) could not be scheduled"
        ]
      },
      {
        "schedule_generation_time": 0.00014901161193847656,
        "conflict_count": 2,
        "conflict_rate": 25.0,
        "deadline_compliance_count": 8,
        "deadline_compliance_rate": 100.0,
        "workload_distribution_std": 0.41738991007401466,
        "daily_hours": {
          "2026-03-11": 5.40246266878725,
          "2026-03-09": 5.700955338733031,
          "2026-03-10": 6.3947654046075435,
          "2026-03-08": 5.908134942660623
        },
        "conflicts": [
          "Task 'Task B5' overlaps with locked block",
          "Task 'Task B6' overlaps with locked block"
        ]
      }
    ],
    "raw_agent": [
      {
        "schedule_generation_time": 0.0007205009460449219,
        "conflict_count": 4,
        "conflict_rate": 50.0,
        "deadline_compliance_count": 4,
        "deadline_compliance_rate": 50.0,
        "workload_distribution_std": 0.2598413266372834,
        "daily_hours": {
          "2026-03-09": 3.8263235201693924,
          "2026-03-12": 3.421645500833725,
          "2026-03-13": 3.2591126741348675,
          "2026-03-11": 3.628188025854103,
          "2026-03-10": 3.9629815769968237,
          "2026-03-08": 3.523330688231006
        },
        "conflicts": [
          "Task 'Task B2' scheduled past deadline (2026-03-11)",
          "Task 'Task B3' scheduled past deadline (2026-03-11)",
          "Task 'Task B7' (ID:7) could not be scheduled",
          "Task 'Task B8' (ID:8) could not be scheduled"
        ]
      },
      {
        "schedule_generation_time": 0.0003705024719238281,
        "conflict_count": 5,
        "conflict_rate": 62.5,
        "deadline_compliance_count": 5,
        "deadline_compliance_rate": 62.5,
        "workload_distribution_std": 1.93918969645943,
        "daily_hours": {
          "2026-03-08": 6.042259548880526,
          "2026-03-09": 4.272532059698238,
          "2026-03-10": 2.168680612591173
        },
        "conflicts": [
          "Task 'Task B1' overlaps with locked block",
          "Task 'Task B3' (ID:3) could not be scheduled",
          "Task 'Task B4' (ID:4) could not be scheduled",
          "Task 'Task B6' (ID:6) could not be scheduled",
          "Task 'Task B7' overlaps with locked block"
        ]
      },
      {
        "schedule_generation_time": 0.0002987384796142578,
        "conflict_count": 3,
        "conflict_rate": 37.5,
        "deadline_compliance_count": 7,
        "deadline_compliance_rate": 87.5,
        "workload_distribution_std": 1.7725998750671792,
        "daily_hours": {
          "2026-03-08": 5.52961410375621,
          "2026-03-09": 5.718238375941733,
          "2026-03-10": 5.764390390072182,
          "2026-03-11": 2.131371418034383
        },
        "conflicts": [
          "Task 'Task B1' overlaps with locked block",
          "Task 'Task B2' (ID:2) could not be scheduled",
          "Task 'Task B4' overlaps with locked block"
        ]
      },
      {
        "schedule_generation_time": 0.0002875328063964844,
        "conflict_count": 5,
        "conflict_rate": 62.5,
        "deadline_compliance_count": 5,
        "deadline_compliance_rate": 62.5,
        "workload_distribution_std": 2.115665027039061,
        "daily_hours": {
          "2026-03-10": 2.409245937352204,
          "2026-03-08": 6.282634579014653,
          "2026-03-09": 5.82098630590154
        },
        "conflicts": [
          "Task 'Task B1' (ID:1) could not be scheduled",
          "Task 'Task B2' overlaps with locked block",
          "Task 'Task B3' (ID:3) could not be scheduled",
          "Task 'Task B4' overlaps with locked block",
          "Task 'Task B8' (ID:8) could not be scheduled"
        ]
      },
      {
        "schedule_generation_time": 0.00028014183044433594,
        "conflict_count": 5,
        "conflict_rate": 62.5,
        "deadline_compliance_count": 3,
        "deadline_compliance_rate": 37.5,
        "workload_distribution_std": 0.3186420193014229,
        "daily_hours": {
          "2026-03-10": 3.56268570575868,
          "2026-03-09": 3.1246776373188636,
          "2026-03-08": 3.7445680748747803
        },
        "conflicts": [
          "Task 'Task B1' (ID:1) could not be scheduled",
          "Task 'Task B3' (ID:3) could not be scheduled",
          "Task 'Task B4' (ID:4) could not be scheduled",
          "Task 'Task B5' (ID:5) could not be scheduled",
          "Task 'Task B8' (ID:8) could not be scheduled"
        ]
      },
      {
        "schedule_generation_time": 0.0003066062927246094,
        "conflict_count": 4,
        "conflict_rate": 50.0,
        "deadline_compliance_count": 5,
        "deadline_compliance_rate": 62.5,
        "workload_distribution_std": 1.5678401977804037,
        "daily_hours": {
          "2026-03-10": 3.374719727605846,
          "2026-03-08": 6.21979278594576,
          "2026-03-09": 5.938982198873802
        },
        "conflicts": [
          "Task 'Task B2' overlaps with locked block",
          "Task 'Task B3' (ID:3) could not be scheduled",
          "Task 'Task B4' (ID:4) could not be scheduled",
          "Task 'Task B6' (ID:6) could not be scheduled"
        ]
      },
      {
        "schedule_generation_time": 0.00029754638671875,
        "conflict_count": 3,
        "conflict_rate": 37.5,
        "deadline_compliance_count": 6,
        "deadline_compliance_rate": 75.0,
        "workload_distribution_std": 1.6657058426621192,
        "daily_hours": {
          "2026-03-11": 3.269543729124809,
          "2026-03-08": 5.654485327768873,
          "2026-03-10": 3.0641840711277397,
          "2026-03-09": 6.356052584058897
        },
        "conflicts": [
          "Task 'Task B2' overlaps with locked block",
          "Task 'Task B3' (ID:3) could not be scheduled",
          "Task 'Task B4' (ID:4) could not be scheduled"
        ]
      },
      {
        "schedule_generation_time": 0.00032329559326171875,
        "conflict_count": 5,
        "conflict_rate": 62.5,
        "deadline_compliance_count": 3,
        "deadline_compliance_rate": 37.5,
        "workload_distribution_std": 0.36589809243684496,
        "daily_hours": {
          "2026-03-10": 3.856064897504122,
          "2026-03-08": 3.847837295600545,
          "2026-03-11": 3.176441316367831,
          "2026-03-09": 3.9871539768145827
        },
        "conflicts": [
          "Task 'Task B2' (ID:2) could not be scheduled",
          "Task 'Task B4' scheduled past deadline (2026-03-10)",
          "Task 'Task B6' (ID:6) could not be scheduled",
          "Task 'Task B7' (ID:7) could not be scheduled",
          "Task 'Task B8' (ID:8) could not be scheduled"
        ]
      },
      {
        "schedule_generation_time": 0.0007135868072509766,
        "conflict_count": 5,
        "conflict_rate": 62.5,
        "deadline_compliance_count": 5,
        "deadline_compliance_rate": 62.5,
        "workload_distribution_std": 2.2306000642452988,
        "daily_hours": {
          "2026-03-08": 6.403115141581219,
          "2026-03-09": 6.075129377875726,
          "2026-03-10": 2.386065169061597
        },
        "conflicts": [
          "Task 'Task B2' (ID:2) could not be scheduled",
          "Task 'Task B3' (ID:3) could not be scheduled",
          "Task 'Task B6' overlaps with locked block",
          "Task 'Task B7' overlaps with locked block",
          "Task 'Task B8' (ID:8) could not be scheduled"
        ]
      },
      {
        "schedule_generation_time": 0.0006570816040039062,
        "conflict_count": 2,
        "conflict_rate": 25.0,
        "deadline_compliance_count": 8,
        "deadline_compliance_rate": 100.0,
        "workload_distribution_std": 0.41738991007401466,
        "daily_hours": {
          "2026-03-11": 5.40246266878725,
          "2026-03-09": 5.700955338733031,
          "2026-03-10": 6.3947654046075435,
          "2026-03-08": 5.908134942660623
        },
        "conflicts": [
          "Task 'Task B5' overlaps with locked block",
          "Task 'Task B6' overlaps with locked block"
        ]
      }
    ]
  },
  "scenario_c": {
    "baseline": {
      "avg_speed": 0.00012400150299072266,
      "avg_tasks_moved": 6.9,
      "avg_efficiency": 31.0
    },
    "agent": {
      "avg_speed": 0.00038361549377441406,
      "avg_tasks_moved": 6.8,
      "avg_efficiency": 32.0
    }
  },
  "scenario_d": {
    "baseline": {
      "avg_speed": 0.00013098716735839843,
      "avg_conflict_rate": 30.0,
      "avg_compliance_rate": 97.27272727272728
    },
    "agent": {
      "avg_speed": 0.0003993511199951172,
      "avg_conflict_rate": 29.09090909090909,
      "avg_compliance_rate": 95.45454545454545
    }
  },
  "scenario_e": {
    "baseline": {
      "avg_generation_time": 0.0010993242263793944,
      "avg_conflict_rate": 87.5,
      "avg_deadline_compliance_rate": 18.75,
      "avg_workload_std": 0.0,
      "std_generation_time": 0.000276830801109296,
      "std_conflict_rate": 0.0
    },
    "agent": {
      "avg_generation_time": 0.0008511543273925781,
      "avg_conflict_rate": 87.5,
      "avg_deadline_compliance_rate": 18.75,
      "avg_workload_std": 0.0,
      "std_generation_time": 0.00014727772615248183,
      "std_conflict_rate": 0.0
    },
    "raw_baseline": [
      {
        "schedule_generation_time": 0.0009968280792236328,
        "conflict_count": 14,
        "conflict_rate": 87.5,
        "deadline_compliance_count": 3,
        "deadline_compliance_rate": 18.75,
        "workload_distribution_std": 0.0,
        "daily_hours": {
          "2026-03-09": 3.0,
          "2026-03-08": 3.0
        },
        "conflicts": [
          "Task 'Literature Review Chapter 1' (ID:1) could not be scheduled",
          "Task 'Set up development environment' overlaps with locked block",
          "Task 'System design document' (ID:4) could not be scheduled",
          "Task 'Database schema design' (ID:5) could not be scheduled",
          "Task 'API specification' (ID:6) could not be scheduled",
          "Task 'Backend core implementation' (ID:7) could not be scheduled",
          "Task 'Frontend UI components' (ID:8) could not be scheduled",
          "Task 'Unit tests' (ID:9) could not be scheduled",
          "Task 'Integration testing' (ID:10) could not be scheduled",
          "Task 'Bug fixes and refinement' (ID:11) could not be scheduled",
          "Task 'Documentation' (ID:12) could not be scheduled",
          "Task 'Run evaluation experiments' (ID:13) could not be scheduled",
          "Task 'Write results chapter' (ID:14) could not be scheduled",
          "Task 'Final dissertation review' (ID:15) could not be scheduled"
        ]
      },
      {
        "schedule_generation_time": 0.0010068416595458984,
        "conflict_count": 14,
        "conflict_rate": 87.5,
        "deadline_compliance_count": 3,
        "deadline_compliance_rate": 18.75,
        "workload_distribution_std": 0.0,
        "daily_hours": {
          "2026-03-09": 3.0,
          "2026-03-08": 3.0
        },
        "conflicts": [
          "Task 'Literature Review Chapter 1' (ID:1) could not be scheduled",
          "Task 'Set up development environment' overlaps with locked block",
          "Task 'System design document' (ID:4) could not be scheduled",
          "Task 'Database schema design' (ID:5) could not be scheduled",
          "Task 'API specification' (ID:6) could not be scheduled",
          "Task 'Backend core implementation' (ID:7) could not be scheduled",
          "Task 'Frontend UI components' (ID:8) could not be scheduled",
          "Task 'Unit tests' (ID:9) could not be scheduled",
          "Task 'Integration testing' (ID:10) could not be scheduled",
          "Task 'Bug fixes and refinement' (ID:11) could not be scheduled",
          "Task 'Documentation' (ID:12) could not be scheduled",
          "Task 'Run evaluation experiments' (ID:13) could not be scheduled",
          "Task 'Write results chapter' (ID:14) could not be scheduled",
          "Task 'Final dissertation review' (ID:15) could not be scheduled"
        ]
      },
      {
        "schedule_generation_time": 0.0009870529174804688,
        "conflict_count": 14,
        "conflict_rate": 87.5,
        "deadline_compliance_count": 3,
        "deadline_compliance_rate": 18.75,
        "workload_distribution_std": 0.0,
        "daily_hours": {
          "2026-03-09": 3.0,
          "2026-03-08": 3.0
        },
        "conflicts": [
          "Task 'Literature Review Chapter 1' (ID:1) could not be scheduled",
          "Task 'Set up development environment' overlaps with locked block",
          "Task 'System design document' (ID:4) could not be scheduled",
          "Task 'Database schema design' (ID:5) could not be scheduled",
          "Task 'API specification' (ID:6) could not be scheduled",
          "Task 'Backend core implementation' (ID:7) could not be scheduled",
          "Task 'Frontend UI components' (ID:8) could not be scheduled",
          "Task 'Unit tests' (ID:9) could not be scheduled",
          "Task 'Integration testing' (ID:10) could not be scheduled",
          "Task 'Bug fixes and refinement' (ID:11) could not be scheduled",
          "Task 'Documentation' (ID:12) could not be scheduled",
          "Task 'Run evaluation experiments' (ID:13) could not be scheduled",
          "Task 'Write results chapter' (ID:14) could not be scheduled",
          "Task 'Final dissertation review' (ID:15) could not be scheduled"
        ]
      },
      {
        "schedule_generation_time": 0.0009834766387939453,
        "conflict_count": 14,
        "conflict_rate": 87.5,
        "deadline_compliance_count": 3,
        "deadline_compliance_rate": 18.75,
        "workload_distribution_std": 0.0,
        "daily_hours": {
          "2026-03-09": 3.0,
          "2026-03-08": 3.0
        },
        "conflicts": [
          "Task 'Literature Review Chapter 1' (ID:1) could not be scheduled",
          "Task 'Set up development environment' overlaps with locked block",
          "Task 'System design document' (ID:4) could not be scheduled",
          "Task 'Database schema design' (ID:5) could not be scheduled",
          "Task 'API specification' (ID:6) could not be scheduled",
          "Task 'Backend core implementation' (ID:7) could not be scheduled",
          "Task 'Frontend UI components' (ID:8) could not be scheduled",
          "Task 'Unit tests' (ID:9) could not be scheduled",
          "Task 'Integration testing' (ID:10) could not be scheduled",
          "Task 'Bug fixes and refinement' (ID:11) could not be scheduled",
          "Task 'Documentation' (ID:12) could not be scheduled",
          "Task 'Run evaluation experiments' (ID:13) could not be scheduled",
          "Task 'Write results chapter' (ID:14) could not be scheduled",
          "Task 'Final dissertation review' (ID:15) could not be scheduled"
        ]
      },
      {
        "schedule_generation_time": 0.0011048316955566406,
        "conflict_count": 14,
        "conflict_rate": 87.5,
        "deadline_compliance_count": 3,
        "deadline_compliance_rate": 18.75,
        "workload_distribution_std": 0.0,
        "daily_hours": {
          "2026-03-09": 3.0,
          "2026-03-08": 3.0
        },
        "conflicts": [
          "Task 'Literature Review Chapter 1' (ID:1) could not be scheduled",
          "Task 'Set up development environment' overlaps with locked block",
          "Task 'System design document' (ID:4) could not be scheduled",
          "Task 'Database schema design' (ID:5) could not be scheduled",
          "Task 'API specification' (ID:6) could not be scheduled",
          "Task 'Backend core implementation' (ID:7) could not be scheduled",
          "Task 'Frontend UI components' (ID:8) could not be scheduled",
          "Task 'Unit tests' (ID:9) could not be scheduled",
          "Task 'Integration testing' (ID:10) could not be scheduled",
          "Task 'Bug fixes and refinement' (ID:11) could not be scheduled",
          "Task 'Documentation' (ID:12) could not be scheduled",
          "Task 'Run evaluation experiments' (ID:13) could not be scheduled",
          "Task 'Write results chapter' (ID:14) could not be scheduled",
          "Task 'Final dissertation review' (ID:15) could not be scheduled"
        ]
      },
      {
        "schedule_generation_time": 0.0010211467742919922,
        "conflict_count": 14,
        "conflict_rate": 87.5,
        "deadline_compliance_count": 3,
        "deadline_compliance_rate": 18.75,
        "workload_distribution_std": 0.0,
        "daily_hours": {
          "2026-03-09": 3.0,
          "2026-03-08": 3.0
        },
        "conflicts": [
          "Task 'Literature Review Chapter 1' (ID:1) could not be scheduled",
          "Task 'Set up development environment' overlaps with locked block",
          "Task 'System design document' (ID:4) could not be scheduled",
          "Task 'Database schema design' (ID:5) could not be scheduled",
          "Task 'API specification' (ID:6) could not be scheduled",
          "Task 'Backend core implementation' (ID:7) could not be scheduled",
          "Task 'Frontend UI components' (ID:8) could not be scheduled",
          "Task 'Unit tests' (ID:9) could not be scheduled",
          "Task 'Integration testing' (ID:10) could not be scheduled",
          "Task 'Bug fixes and refinement' (ID:11) could not be scheduled",
          "Task 'Documentation' (ID:12) could not be scheduled",
          "Task 'Run evaluation experiments' (ID:13) could not be scheduled",
          "Task 'Write results chapter' (ID:14) could not be scheduled",
          "Task 'Final dissertation review' (ID:15) could not be scheduled"
        ]
      },
      {
        "schedule_generation_time": 0.0010035037994384766,
        "conflict_count": 14,
        "conflict_rate": 87.5,
        "deadline_compliance_count": 3,
        "deadline_compliance_rate": 18.75,
        "workload_distribution_std": 0.0,
        "daily_hours": {
          "2026-03-09": 3.0,
          "2026-03-08": 3.0
        },
        "conflicts": [
          "Task 'Literature Review Chapter 1' (ID:1) could not be scheduled",
          "Task 'Set up development environment' overlaps with locked block",
          "Task 'System design document' (ID:4) could not be scheduled",
          "Task 'Database schema design' (ID:5) could not be scheduled",
          "Task 'API specification' (ID:6) could not be scheduled",
          "Task 'Backend core implementation' (ID:7) could not be scheduled",
          "Task 'Frontend UI components' (ID:8) could not be scheduled",
          "Task 'Unit tests' (ID:9) could not be scheduled",
          "Task 'Integration testing' (ID:10) could not be scheduled",
          "Task 'Bug fixes and refinement' (ID:11) could not be scheduled",
          "Task 'Documentation' (ID:12) could not be scheduled",
          "Task 'Run evaluation experiments' (ID:13) could not be scheduled",
          "Task 'Write results chapter' (ID:14) could not be scheduled",
          "Task 'Final dissertation review' (ID:15) could not be scheduled"
        ]
      },
      {
        "schedule_generation_time": 0.0018811225891113281,
        "conflict_count": 14,
        "conflict_rate": 87.5,
        "deadline_compliance_count": 3,
        "deadline_compliance_rate": 18.75,
        "workload_distribution_std": 0.0,
        "daily_hours": {
          "2026-03-09": 3.0,
          "2026-03-08": 3.0
        },
        "conflicts": [
          "Task 'Literature Review Chapter 1' (ID:1) could not be scheduled",
          "Task 'Set up development environment' overlaps with locked block",
          "Task 'System design document' (ID:4) could not be scheduled",
          "Task 'Database schema design' (ID:5) could not be scheduled",
          "Task 'API specification' (ID:6) could not be scheduled",
          "Task 'Backend core implementation' (ID:7) could not be scheduled",
          "Task 'Frontend UI components' (ID:8) could not be scheduled",
          "Task 'Unit tests' (ID:9) could not be scheduled",
          "Task 'Integration testing' (ID:10) could not be scheduled",
          "Task 'Bug fixes and refinement' (ID:11) could not be scheduled",
          "Task 'Documentation' (ID:12) could not be scheduled",
          "Task 'Run evaluation experiments' (ID:13) could not be scheduled",
          "Task 'Write results chapter' (ID:14) could not be scheduled",
          "Task 'Final dissertation review' (ID:15) could not be scheduled"
        ]
      },
      {
        "schedule_generation_time": 0.0010066032409667969,
        "conflict_count": 14,
        "conflict_rate": 87.5,
        "deadline_compliance_count": 3,
        "deadline_compliance_rate": 18.75,
        "workload_distribution_std": 0.0,
        "daily_hours": {
          "2026-03-09": 3.0,
          "2026-03-08": 3.0
        },
        "conflicts": [
          "Task 'Literature Review Chapter 1' (ID:1) could not be scheduled",
          "Task 'Set up development environment' overlaps with locked block",
          "Task 'System design document' (ID:4) could not be scheduled",
          "Task 'Database schema design' (ID:5) could not be scheduled",
          "Task 'API specification' (ID:6) could not be scheduled",
          "Task 'Backend core implementation' (ID:7) could not be scheduled",
          "Task 'Frontend UI components' (ID:8) could not be scheduled",
          "Task 'Unit tests' (ID:9) could not be scheduled",
          "Task 'Integration testing' (ID:10) could not be scheduled",
          "Task 'Bug fixes and refinement' (ID:11) could not be scheduled",
          "Task 'Documentation' (ID:12) could not be scheduled",
          "Task 'Run evaluation experiments' (ID:13) could not be scheduled",
          "Task 'Write results chapter' (ID:14) could not be scheduled",
          "Task 'Final dissertation review' (ID:15) could not be scheduled"
        ]
      },
      {
        "schedule_generation_time": 0.0010018348693847656,
        "conflict_count": 14,
        "conflict_rate": 87.5,
        "deadline_compliance_count": 3,
        "deadline_compliance_rate": 18.75,
        "workload_distribution_std": 0.0,
        "daily_hours": {
          "2026-03-09": 3.0,
          "2026-03-08": 3.0
        },
        "conflicts": [
          "Task 'Literature Review Chapter 1' (ID:1) could not be scheduled",
          "Task 'Set up development environment' overlaps with locked block",
          "Task 'System design document' (ID:4) could not be scheduled",
          "Task 'Database schema design' (ID:5) could not be scheduled",
          "Task 'API specification' (ID:6) could not be scheduled",
          "Task 'Backend core implementation' (ID:7) could not be scheduled",
          "Task 'Frontend UI components' (ID:8) could not be scheduled",
          "Task 'Unit tests' (ID:9) could not be scheduled",
          "Task 'Integration testing' (ID:10) could not be scheduled",
          "Task 'Bug fixes and refinement' (ID:11) could not be scheduled",
          "Task 'Documentation' (ID:12) could not be scheduled",
          "Task 'Run evaluation experiments' (ID:13) could not be scheduled",
          "Task 'Write results chapter' (ID:14) could not be scheduled",
          "Task 'Final dissertation review' (ID:15) could not be scheduled"
        ]
      }
    ],
    "raw_agent": [
      {
        "schedule_generation_time": 0.0007822513580322266,
        "conflict_count": 14,
        "conflict_rate": 87.5,
        "deadline_compliance_count": 3,
        "deadline_compliance_rate": 18.75,
        "workload_distribution_std": 0.0,
        "daily_hours": {
          "2026-03-09": 3.0,
          "2026-03-08": 3.0
        },
        "conflicts": [
          "Task 'Literature Review Chapter 1' (ID:1) could not be scheduled",
          "Task 'Set up development environment' overlaps with locked block",
          "Task 'System design document' (ID:4) could not be scheduled",
          "Task 'Database schema design' (ID:5) could not be scheduled",
          "Task 'API specification' (ID:6) could not be scheduled",
          "Task 'Backend core implementation' (ID:7) could not be scheduled",
          "Task 'Frontend UI components' (ID:8) could not be scheduled",
          "Task 'Unit tests' (ID:9) could not be scheduled",
          "Task 'Integration testing' (ID:10) could not be scheduled",
          "Task 'Bug fixes and refinement' (ID:11) could not be scheduled",
          "Task 'Documentation' (ID:12) could not be scheduled",
          "Task 'Run evaluation experiments' (ID:13) could not be scheduled",
          "Task 'Write results chapter' (ID:14) could not be scheduled",
          "Task 'Final dissertation review' (ID:15) could not be scheduled"
        ]
      },
      {
        "schedule_generation_time": 0.0007615089416503906,
        "conflict_count": 14,
        "conflict_rate": 87.5,
        "deadline_compliance_count": 3,
        "deadline_compliance_rate": 18.75,
        "workload_distribution_std": 0.0,
        "daily_hours": {
          "2026-03-09": 3.0,
          "2026-03-08": 3.0
        },
        "conflicts": [
          "Task 'Literature Review Chapter 1' (ID:1) could not be scheduled",
          "Task 'Set up development environment' overlaps with locked block",
          "Task 'System design document' (ID:4) could not be scheduled",
          "Task 'Database schema design' (ID:5) could not be scheduled",
          "Task 'API specification' (ID:6) could not be scheduled",
          "Task 'Backend core implementation' (ID:7) could not be scheduled",
          "Task 'Frontend UI components' (ID:8) could not be scheduled",
          "Task 'Unit tests' (ID:9) could not be scheduled",
          "Task 'Integration testing' (ID:10) could not be scheduled",
          "Task 'Bug fixes and refinement' (ID:11) could not be scheduled",
          "Task 'Documentation' (ID:12) could not be scheduled",
          "Task 'Run evaluation experiments' (ID:13) could not be scheduled",
          "Task 'Write results chapter' (ID:14) could not be scheduled",
          "Task 'Final dissertation review' (ID:15) could not be scheduled"
        ]
      },
      {
        "schedule_generation_time": 0.000782012939453125,
        "conflict_count": 14,
        "conflict_rate": 87.5,
        "deadline_compliance_count": 3,
        "deadline_compliance_rate": 18.75,
        "workload_distribution_std": 0.0,
        "daily_hours": {
          "2026-03-09": 3.0,
          "2026-03-08": 3.0
        },
        "conflicts": [
          "Task 'Literature Review Chapter 1' (ID:1) could not be scheduled",
          "Task 'Set up development environment' overlaps with locked block",
          "Task 'System design document' (ID:4) could not be scheduled",
          "Task 'Database schema design' (ID:5) could not be scheduled",
          "Task 'API specification' (ID:6) could not be scheduled",
          "Task 'Backend core implementation' (ID:7) could not be scheduled",
          "Task 'Frontend UI components' (ID:8) could not be scheduled",
          "Task 'Unit tests' (ID:9) could not be scheduled",
          "Task 'Integration testing' (ID:10) could not be scheduled",
          "Task 'Bug fixes and refinement' (ID:11) could not be scheduled",
          "Task 'Documentation' (ID:12) could not be scheduled",
          "Task 'Run evaluation experiments' (ID:13) could not be scheduled",
          "Task 'Write results chapter' (ID:14) could not be scheduled",
          "Task 'Final dissertation review' (ID:15) could not be scheduled"
        ]
      },
      {
        "schedule_generation_time": 0.0007781982421875,
        "conflict_count": 14,
        "conflict_rate": 87.5,
        "deadline_compliance_count": 3,
        "deadline_compliance_rate": 18.75,
        "workload_distribution_std": 0.0,
        "daily_hours": {
          "2026-03-09": 3.0,
          "2026-03-08": 3.0
        },
        "conflicts": [
          "Task 'Literature Review Chapter 1' (ID:1) could not be scheduled",
          "Task 'Set up development environment' overlaps with locked block",
          "Task 'System design document' (ID:4) could not be scheduled",
          "Task 'Database schema design' (ID:5) could not be scheduled",
          "Task 'API specification' (ID:6) could not be scheduled",
          "Task 'Backend core implementation' (ID:7) could not be scheduled",
          "Task 'Frontend UI components' (ID:8) could not be scheduled",
          "Task 'Unit tests' (ID:9) could not be scheduled",
          "Task 'Integration testing' (ID:10) could not be scheduled",
          "Task 'Bug fixes and refinement' (ID:11) could not be scheduled",
          "Task 'Documentation' (ID:12) could not be scheduled",
          "Task 'Run evaluation experiments' (ID:13) could not be scheduled",
          "Task 'Write results chapter' (ID:14) could not be scheduled",
          "Task 'Final dissertation review' (ID:15) could not be scheduled"
        ]
      },
      {
        "schedule_generation_time": 0.0009415149688720703,
        "conflict_count": 14,
        "conflict_rate": 87.5,
        "deadline_compliance_count": 3,
        "deadline_compliance_rate": 18.75,
        "workload_distribution_std": 0.0,
        "daily_hours": {
          "2026-03-09": 3.0,
          "2026-03-08": 3.0
        },
        "conflicts": [
          "Task 'Literature Review Chapter 1' (ID:1) could not be scheduled",
          "Task 'Set up development environment' overlaps with locked block",
          "Task 'System design document' (ID:4) could not be scheduled",
          "Task 'Database schema design' (ID:5) could not be scheduled",
          "Task 'API specification' (ID:6) could not be scheduled",
          "Task 'Backend core implementation' (ID:7) could not be scheduled",
          "Task 'Frontend UI components' (ID:8) could not be scheduled",
          "Task 'Unit tests' (ID:9) could not be scheduled",
          "Task 'Integration testing' (ID:10) could not be scheduled",
          "Task 'Bug fixes and refinement' (ID:11) could not be scheduled",
          "Task 'Documentation' (ID:12) could not be scheduled",
          "Task 'Run evaluation experiments' (ID:13) could not be scheduled",
          "Task 'Write results chapter' (ID:14) could not be scheduled",
          "Task 'Final dissertation review' (ID:15) could not be scheduled"
        ]
      },
      {
        "schedule_generation_time": 0.0009474754333496094,
        "conflict_count": 14,
        "conflict_rate": 87.5,
        "deadline_compliance_count": 3,
        "deadline_compliance_rate": 18.75,
        "workload_distribution_std": 0.0,
        "daily_hours": {
          "2026-03-09": 3.0,
          "2026-03-08": 3.0
        },
        "conflicts": [
          "Task 'Literature Review Chapter 1' (ID:1) could not be scheduled",
          "Task 'Set up development environment' overlaps with locked block",
          "Task 'System design document' (ID:4) could not be scheduled",
          "Task 'Database schema design' (ID:5) could not be scheduled",
          "Task 'API specification' (ID:6) could not be scheduled",
          "Task 'Backend core implementation' (ID:7) could not be scheduled",
          "Task 'Frontend UI components' (ID:8) could not be scheduled",
          "Task 'Unit tests' (ID:9) could not be scheduled",
          "Task 'Integration testing' (ID:10) could not be scheduled",
          "Task 'Bug fixes and refinement' (ID:11) could not be scheduled",
          "Task 'Documentation' (ID:12) could not be scheduled",
          "Task 'Run evaluation experiments' (ID:13) could not be scheduled",
          "Task 'Write results chapter' (ID:14) could not be scheduled",
          "Task 'Final dissertation review' (ID:15) could not be scheduled"
        ]
      },
      {
        "schedule_generation_time": 0.0007524490356445312,
        "conflict_count": 14,
        "conflict_rate": 87.5,
        "deadline_compliance_count": 3,
        "deadline_compliance_rate": 18.75,
        "workload_distribution_std": 0.0,
        "daily_hours": {
          "2026-03-09": 3.0,
          "2026-03-08": 3.0
        },
        "conflicts": [
          "Task 'Literature Review Chapter 1' (ID:1) could not be scheduled",
          "Task 'Set up development environment' overlaps with locked block",
          "Task 'System design document' (ID:4) could not be scheduled",
          "Task 'Database schema design' (ID:5) could not be scheduled",
          "Task 'API specification' (ID:6) could not be scheduled",
          "Task 'Backend core implementation' (ID:7) could not be scheduled",
          "Task 'Frontend UI components' (ID:8) could not be scheduled",
          "Task 'Unit tests' (ID:9) could not be scheduled",
          "Task 'Integration testing' (ID:10) could not be scheduled",
          "Task 'Bug fixes and refinement' (ID:11) could not be scheduled",
          "Task 'Documentation' (ID:12) could not be scheduled",
          "Task 'Run evaluation experiments' (ID:13) could not be scheduled",
          "Task 'Write results chapter' (ID:14) could not be scheduled",
          "Task 'Final dissertation review' (ID:15) could not be scheduled"
        ]
      },
      {
        "schedule_generation_time": 0.0007910728454589844,
        "conflict_count": 14,
        "conflict_rate": 87.5,
        "deadline_compliance_count": 3,
        "deadline_compliance_rate": 18.75,
        "workload_distribution_std": 0.0,
        "daily_hours": {
          "2026-03-09": 3.0,
          "2026-03-08": 3.0
        },
        "conflicts": [
          "Task 'Literature Review Chapter 1' (ID:1) could not be scheduled",
          "Task 'Set up development environment' overlaps with locked block",
          "Task 'System design document' (ID:4) could not be scheduled",
          "Task 'Database schema design' (ID:5) could not be scheduled",
          "Task 'API specification' (ID:6) could not be scheduled",
          "Task 'Backend core implementation' (ID:7) could not be scheduled",
          "Task 'Frontend UI components' (ID:8) could not be scheduled",
          "Task 'Unit tests' (ID:9) could not be scheduled",
          "Task 'Integration testing' (ID:10) could not be scheduled",
          "Task 'Bug fixes and refinement' (ID:11) could not be scheduled",
          "Task 'Documentation' (ID:12) could not be scheduled",
          "Task 'Run evaluation experiments' (ID:13) could not be scheduled",
          "Task 'Write results chapter' (ID:14) could not be scheduled",
          "Task 'Final dissertation review' (ID:15) could not be scheduled"
        ]
      },
      {
        "schedule_generation_time": 0.0012159347534179688,
        "conflict_count": 14,
        "conflict_rate": 87.5,
        "deadline_compliance_count": 3,
        "deadline_compliance_rate": 18.75,
        "workload_distribution_std": 0.0,
        "daily_hours": {
          "2026-03-09": 3.0,
          "2026-03-08": 3.0
        },
        "conflicts": [
          "Task 'Literature Review Chapter 1' (ID:1) could not be scheduled",
          "Task 'Set up development environment' overlaps with locked block",
          "Task 'System design document' (ID:4) could not be scheduled",
          "Task 'Database schema design' (ID:5) could not be scheduled",
          "Task 'API specification' (ID:6) could not be scheduled",
          "Task 'Backend core implementation' (ID:7) could not be scheduled",
          "Task 'Frontend UI components' (ID:8) could not be scheduled",
          "Task 'Unit tests' (ID:9) could not be scheduled",
          "Task 'Integration testing' (ID:10) could not be scheduled",
          "Task 'Bug fixes and refinement' (ID:11) could not be scheduled",
          "Task 'Documentation' (ID:12) could not be scheduled",
          "Task 'Run evaluation experiments' (ID:13) could not be scheduled",
          "Task 'Write results chapter' (ID:14) could not be scheduled",
          "Task 'Final dissertation review' (ID:15) could not be scheduled"
        ]
      },
      {
        "schedule_generation_time": 0.000759124755859375,
        "conflict_count": 14,
        "conflict_rate": 87.5,
        "deadline_compliance_count": 3,
        "deadline_compliance_rate": 18.75,
        "workload_distribution_std": 0.0,
        "daily_hours": {
          "2026-03-09": 3.0,
          "2026-03-08": 3.0
        },
        "conflicts": [
          "Task 'Literature Review Chapter 1' (ID:1) could not be scheduled",
          "Task 'Set up development environment' overlaps with locked block",
          "Task 'System design document' (ID:4) could not be scheduled",
          "Task 'Database schema design' (ID:5) could not be scheduled",
          "Task 'API specification' (ID:6) could not be scheduled",
          "Task 'Backend core implementation' (ID:7) could not be scheduled",
          "Task 'Frontend UI components' (ID:8) could not be scheduled",
          "Task 'Unit tests' (ID:9) could not be scheduled",
          "Task 'Integration testing' (ID:10) could not be scheduled",
          "Task 'Bug fixes and refinement' (ID:11) could not be scheduled",
          "Task 'Documentation' (ID:12) could not be scheduled",
          "Task 'Run evaluation experiments' (ID:13) could not be scheduled",
          "Task 'Write results chapter' (ID:14) could not be scheduled",
          "Task 'Final dissertation review' (ID:15) could not be scheduled"
        ]
      }
    ]
  },
  "summary": {
    "hypothesis_h1_supported": false,
    "hypothesis_h2_supported": true,
    "hypothesis_h3_supported": true,
    "details": {
      "generation_time_comparison": {
        "agent": 0.0005606651306152344,
        "baseline": 0.0001802206039428711,
        "improvement_pct": -211.09935176610662
      },
      "quality_comparison": {
        "agent_conflict_rate": 28.0,
        "baseline_conflict_rate": 30.0,
        "agent_compliance_rate": 98.0,
        "baseline_compliance_rate": 98.0
      },
      "adaptation_comparison": {
        "agent_efficiency": 32.0,
        "baseline_efficiency": 31.0
      }
    }
  }
}