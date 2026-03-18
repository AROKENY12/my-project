{
  "generated_at": "2026-03-08T22:59:38.789523Z",
  "latency": {
    "GET /api/tasks": {
      "avg_ms": 0.86,
      "p50_ms": 0.83,
      "p95_ms": 0.99,
      "max_ms": 2.33
    },
    "GET /api/tasks/conflicts": {
      "avg_ms": 0.81,
      "p50_ms": 0.78,
      "p95_ms": 0.93,
      "max_ms": 1.4
    },
    "GET /api/schedule": {
      "avg_ms": 0.91,
      "p50_ms": 0.78,
      "p95_ms": 0.94,
      "max_ms": 17.05
    },
    "POST /api/chat": {
      "avg_ms": 0.81,
      "p50_ms": 0.78,
      "p95_ms": 0.99,
      "max_ms": 1.42
    },
    "POST /api/schedule/adapt": {
      "avg_ms": 0.79,
      "p50_ms": 0.76,
      "p95_ms": 0.97,
      "max_ms": 1.42
    }
  },
  "uplift": {
    "scenario_a": {
      "conflict_rate_uplift_pct_points": 3.75,
      "deadline_compliance_uplift_pct_points": 0.0
    },
    "scenario_e": {
      "conflict_rate_uplift_pct_points": 0.0,
      "deadline_compliance_uplift_pct_points": 0.0,
      "workload_balance_std_uplift_hours": 0.0
    },
    "scenario_c": {
      "adaptation_efficiency_uplift_pct_points": 0.0,
      "adaptation_speed_uplift_ms": -0.2
    }
  },
  "scale": {
    "10": {
      "agent_avg_ms": 0.33,
      "baseline_avg_ms": 0.08,
      "agent_p95_ms": 0.35,
      "agent_avg_conflict_rate": 0.0,
      "baseline_avg_conflict_rate": 0.0
    },
    "25": {
      "agent_avg_ms": 0.6,
      "baseline_avg_ms": 0.31,
      "agent_p95_ms": 0.54,
      "agent_avg_conflict_rate": 0.0,
      "baseline_avg_conflict_rate": 0.0
    },
    "50": {
      "agent_avg_ms": 0.76,
      "baseline_avg_ms": 0.86,
      "agent_p95_ms": 0.78,
      "agent_avg_conflict_rate": 0.0,
      "baseline_avg_conflict_rate": 0.0
    },
    "100": {
      "agent_avg_ms": 8.08,
      "baseline_avg_ms": 2.33,
      "agent_p95_ms": 8.2,
      "agent_avg_conflict_rate": 75.0,
      "baseline_avg_conflict_rate": 76.0
    }
  },
  "usability": {
    "metric_key": "taskCreationDurationsSec",
    "metric_description": "Per-task creation completion time in seconds (client-side)",
    "target_seconds": 30,
    "implementation_note": "Average is shown in the Tasks tab as 'Avg task creation time'."
  }
}