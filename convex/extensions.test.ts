import { describe, expect, it } from 'vitest'
import type { Doc } from './_generated/dataModel'
import { __test } from './extensions'

const baseResource: Doc<'resources'> = {
  _id: 'resources:1',
  _creationTime: 0,
  type: 'extension',
  slug: 'demo',
  displayName: 'Demo',
  summary: 'Summary',
  ownerUserId: 'users:1',
  ownerHandle: 'demo',
  softDeletedAt: undefined,
  moderationStatus: 'active',
  moderationFlags: undefined,
  statsDownloads: 0,
  statsStars: 0,
  statsInstallsCurrent: undefined,
  statsInstallsAllTime: undefined,
  stats: {
    downloads: 0,
    installsCurrent: undefined,
    installsAllTime: undefined,
    stars: 0,
    versions: 1,
    comments: 0,
  },
  createdAt: 1,
  updatedAt: 1,
}

describe('toPublicExtension', () => {
  it('filters out hidden extensions', () => {
    const resource = { ...baseResource, moderationStatus: 'hidden' }
    expect(__test.toPublicExtension(resource)).toBeNull()
  })

  it('filters out blocked extensions', () => {
    const resource = { ...baseResource, moderationFlags: ['blocked.malware'] }
    expect(__test.toPublicExtension(resource)).toBeNull()
  })

  it('returns public data for active extensions', () => {
    const resource = { ...baseResource }
    expect(__test.toPublicExtension(resource)?.slug).toBe('demo')
  })
})
