import { describe, expect, it } from 'vitest'
import type { Doc } from '../_generated/dataModel'
import { toPublicSoul } from './public'

const baseSoul: Doc<'souls'> = {
  _id: 'souls:1',
  _creationTime: 0,
  slug: 'north-star',
  displayName: 'North Star',
  summary: 'Notes',
  ownerUserId: 'users:1',
  latestVersionId: undefined,
  tags: {},
  softDeletedAt: undefined,
  moderationStatus: 'active',
  moderationFlags: undefined,
  stats: {
    downloads: 0,
    stars: 0,
    versions: 1,
    comments: 0,
  },
  createdAt: 1,
  updatedAt: 1,
}

describe('toPublicSoul', () => {
  it('returns null for hidden souls', () => {
    const soul = { ...baseSoul, moderationStatus: 'hidden' }
    expect(toPublicSoul(soul)).toBeNull()
  })

  it('returns null for flagged souls', () => {
    const soul = { ...baseSoul, moderationFlags: ['blocked.malware'] }
    expect(toPublicSoul(soul)).toBeNull()
  })

  it('returns public data for active souls', () => {
    const soul = { ...baseSoul }
    expect(toPublicSoul(soul)?.slug).toBe('north-star')
  })
})
