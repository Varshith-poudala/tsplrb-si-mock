// Storage utility for user-partitioned exam progress
export const ALL_TEST_IDS = [
  'demo-test-50',
  'tsplrb-si-mock-full-200',
  'tsplrb-si-mock-full-200-2',
  'tsplrb-si-mock-full-200-3',
  'tsplrb-si-mock-full-200-4',
  'tsplrb-si-mock-full-200-5',
  'tsplrb-si-mock-full-200-6',
  'tsplrb-si-mock-full-200-7',
  'tsplrb-si-mock-full-200-8',
  'tsplrb-si-mock-full-200-9',
];

export function getExamProgressKey(userEmail, testId) {
  if (!userEmail) return `exam_progress_anon_${testId}`;
  const cleanEmail = String(userEmail).toLowerCase().trim().replace(/[^a-z0-9]/g, '_');
  return `exam_progress_${cleanEmail}_${testId}`;
}

export function clearLegacyUnscopedProgress() {
  try {
    ALL_TEST_IDS.forEach((id) => {
      localStorage.removeItem(`exam_progress_${id}`);
    });
  } catch (e) {
    console.warn('Failed to clear legacy unscoped exam progress:', e);
  }
}
